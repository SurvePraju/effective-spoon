from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PersonalChatRoom(models.Model):
    users = models.ManyToManyField("auth.User")


class Messages(models.Model):
    room_number = models.ForeignKey(PersonalChatRoom, on_delete=models.CASCADE)
    sender = models.CharField(max_length=50)
    text = models.TextField()
