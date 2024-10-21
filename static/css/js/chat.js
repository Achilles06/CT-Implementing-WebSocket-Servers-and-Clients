var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function() {
    console.log('Connected to the server');
});

function sendMessage() {
    var input = document.getElementById('message-input').value;
    socket.emit('message', {'user': 'JohnDoe', 'message': input});
}

socket.on('message', function(data) {
    var chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += '<p>' + data.user + ': ' + data.message + '</p>';
});
