from flask import Blueprint, render_template
from flask_login import login_required

# 建立(註冊)路由的函式
RoomRoutes = Blueprint('RoomRoutes', __name__, template_folder="templates", static_folder="static")



@RoomRoutes.route('/index', methods=['GET'])
#@login_required
def index():
    return render_template('ChatRoom.html')


@RoomRoutes.route('/getMemberList', methods=['GET'])
def get_member_list():
    return '{"_id":["0","2","3","5"]}'


@login_required
@RoomRoutes.route('/create', methods=['POST'])
def create():
    return "create_chat_room()"


@login_required
@RoomRoutes.route('/rename', methods=['POST'])
def rename():
    return "rename_chat_room()"


@login_required
@RoomRoutes.route('/delete', methods=['POST'])
def delete():
    return "delete_chat_room()"


@RoomRoutes.route('/addMember', methods=['POST'])
def add_member():
    return "chat_room_add_member()"


@RoomRoutes.route('/removeMember', methods=['POST'])
def remove_member():
    return "chat_room_remove_member()"
