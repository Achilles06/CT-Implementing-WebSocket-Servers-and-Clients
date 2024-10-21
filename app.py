from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# HashMap storage for messages
message_storage = {}

@app.route('/')
def index():
    return render_template('index.html')

# Event handler for receiving messages
@socketio.on('message')
def handle_message_event(data):
    user = data.get('user')
    message = data.get('message')

    if user and message:
        # Store message in HashMap
        if user in message_storage:
            message_storage[user].append(message)
        else:
            message_storage[user] = [message]
        
        # Broadcast message to all clients
        emit('message', {'user': user, 'message': message}, broadcast=True)

# Event handler for retrieving all messages for a specific user
@socketio.on('get_all_messages')
def handle_get_messages_event(data):
    user = data.get('user')
    if user and user in message_storage:
        messages = message_storage[user]
        emit('user_messages', {'user': user, 'messages': messages})
    else:
        emit('user_messages', {'user': user, 'messages': []})

if __name__ == '__main__':
    socketio.run(app)
