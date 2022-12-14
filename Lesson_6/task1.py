from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, emit
from database import addMessageToDB, prepareDataBaseForChat, getMessagesInHtmlTags

NAME_DB = "Chat.db"

app = Flask("Chat")
socketio = SocketIO(app)
prepareDataBaseForChat(NAME_DB)

@app.route('/')
def index():
    return render_template("task1.html", message = getMessagesInHtmlTags(NAME_DB))

@app.route('/getmessages')
def get():
    return getMessagesInHtmlTags(NAME_DB)

@socketio.on('send message')
def send(dct):
    print("send")
    name = dct["name"]
    text = dct["text"]
    addMessageToDB(NAME_DB, name, text)
    return None

socketio.run(app = app, host="0.0.0.0", port=8080, debug=True)