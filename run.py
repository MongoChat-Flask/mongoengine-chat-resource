import os
import datetime
from flask_socketio import send, join_room, leave_room, emit
from time import localtime, strftime
from app import app, socketio
from flask import url_for
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
    messagejson = {"username": username, "msg": msg, "time_stamp": time_stamp}
    # Insert Message
    from models.Message import Message
    mongoMsg = Message(Message_creator=username, Context=msg, Timestamp=datetime.datetime.utcnow())
    mongoMsg.save()
    send(messagejson, room=room)


# @socketio.on('delete-event')  # 對應 JS 的 socket.emit('delete')
# def delete(data):
#     print(f'id: {data}')
#

@socketio.on('join')  # 對應 JS 的 socket.emit('join')
def join(data):
    join_room(data['room'])
    time_stamp = strftime('%b-%d %I:%M%p', localtime())
    send({
        'username': '系統',
        'msg': data['username'] + " has joined the " + data['room'] + " room.",
        'time_stamp': time_stamp
    }, room=data['room'])


@socketio.on('leave')  # 對應 JS 的 socket.emit('leave')
def join(data):
    leave_room(data['room'])
    send({
        'msg': data['username'] + " has left the " + data['room'] + " room."
    }, room=data['room'])  # 傳送至指定的room


# def MongoScheduledTask():
#     print("此任务每 3600 秒运行一次!\n任務: 清除過期不合法帳戶.")


if __name__ == '__main__':
    socketio.run(app, debug=True)
    # app.run()
