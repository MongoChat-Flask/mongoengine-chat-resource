from flask_socketio import send, join_room, leave_room, emit
from time import localtime, strftime
from app import app, socketio
from flask import url_for, render_template
from werkzeug.utils import redirect


@app.route('/')
def startpoint():
    return redirect(url_for('UserRoutes.start'))



@socketio.on('message')
def Handle_Messasge(data):
    print(f"\n\n{data}\n\n")
    """Broadcast messages"""
    msg = data["msg"]
    username = data["username"]
    room = data["room"]
    # Set timestamp
    time_stamp = strftime('%b-%d %I:%M%p', localtime())
    send({"username": username, "msg": msg, "time_stamp": time_stamp}, room=room)


@socketio.on('join')  # 對應 JS 的 socket.emit('join')
def join(data):
    join_room(data['room'])
    send({
        'msg': data['username'] + " has joined the " + data['room'] + " room.",
    }, room=data['room'])


@socketio.on('leave')  # 對應 JS 的 socket.emit('leave')
def join(data):
    leave_room(data['room'])
    send({
        'msg': data['username'] + " has left the " + data['room'] + " room."
    }, room=data['room'])  # 傳送至指定的room


if __name__ == '__main__':
    socketio.run(app, debug=True)
