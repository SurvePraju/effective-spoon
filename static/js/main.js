

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

document.querySelector("#message").addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        document.querySelector("#send-message").submit();
    }

});



