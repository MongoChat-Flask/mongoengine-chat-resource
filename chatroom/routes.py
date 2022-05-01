from flask import Blueprint

from chatroom.ChatRoomController import *

# 建立(註冊)路由的函式
RoomRoutes = Blueprint('RoomRoutes', __name__)


@RoomRoutes.route('/create', methods=['GET'])
def create():
    return "CreateRoom()"
