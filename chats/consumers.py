from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json
from . models import *


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        owner = self.scope["user"]

        owner_obj = await self.get_user(username=owner)

        print(f"Owner:{owner_obj.id}")

        other_user = self.scope["url_route"]["kwargs"]["room_name"]
        other_user_obj = await self.get_user(username=other_user)

        print(f"other_user:{other_user_obj.id}")

        temp_room_name = await self.get_or_create_async(user1=owner_obj, user2=other_user_obj)

        print(temp_room_name)
        self.room_name = temp_room_name
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    @database_sync_to_async
    def get_or_create_async(self, user1, user2):
        print(f"Users: {user1.username}, {user2.username}")
        existing_obj = PersonalChatRoom.objects.filter(
            users=user1).filter(users=user2).first()

        if existing_obj:
            print(f"Existing Room ID: {existing_obj.id}")
            return existing_obj.id
        else:
            new_obj = PersonalChatRoom.objects.create()
            new_obj.users.add(user1, user2)
            new_obj.save()
            print(f"New Room ID: {new_obj.id}")
            return new_obj.id

    @database_sync_to_async
    def get_user(self, username):
        return User.objects.get(username=username)

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
