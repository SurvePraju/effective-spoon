

let insertTextBox = function () {
    let chatboxSearchButton = document.querySelector(".chatbox-search");
    let existingSearchInput = document.querySelector("#search-chat-message");
    if (existingSearchInput) {
        chatboxSearchButton.removeChild(existingSearchInput);
    }
    let searchChatInput = document.createElement("input");
    searchChatInput.type = "search";
    searchChatInput.id = "search-chat-message";
    searchChatInput.placeholder = "Search in Chat"
    searchChatInput.focus();
    chatboxSearchButton.appendChild(searchChatInput);
}



document.querySelectorAll(".single-user").forEach((user) => {
    user.addEventListener("click", (e) => {
        // Get the username from the clicked element
        var userName = e.target.innerHTML;
        // console.log(document.querySelector(".chatbox").classList);
        // Show the chatbox and hide the user-not-selected container
        // document.querySelector(".chatbox").classList.remove("hide");
        // document.querySelector(".user-not-selected").classList.add("hide");

        // Update the username in the chatbox
        // document.querySelector(".chatbox-user h1").innerHTML = userName;
        window.location.pathname = "/" + userName + "/";
        console.log(window.location.pathname);
    });
});





// Send Message to the Consumer  
document.querySelector("#message").addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        const inputValue = document.querySelector("#message");
        console.log(inputValue.value);
        chatSocket.send(JSON.stringify({ "message": inputValue.value, "sender": roomName }));
        inputValue.value = "";
    }
});




const roomName = document.querySelector(".chatbox-user h1").innerHTML;
console.log(roomName);
const chatSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/" + roomName + "/"
)

chatSocket.onopen = function (e) {
    console.log("Connection is Opened")
}


chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    console.log(data.message);

    const chatBody = document.querySelector(".message-body");

    // Create a new message block
    const newMessageBlock = document.createElement("div");

    // Uncomment and modify this section based on your requirements
    // const roomName = "someRoomName"; // Replace with the actual room name
    // if (data.sender === roomName) {
    newMessageBlock.classList.add("message-sent");
    // } else {
    //     newMessageBlock.classList.add("message-received");
    // }

    // Create a span to hold the message content
    const messageHolder = document.createElement("span");

    // Parse the JSON string and get the 'message' property
    const messageText = data.message

    // Set the innerHTML of the span with the extracted message text
    messageHolder.innerHTML = messageText;

    // Append the span to the new message block
    newMessageBlock.appendChild(messageHolder);

    // Append the new message block to the chat body
    chatBody.appendChild(newMessageBlock);
}




