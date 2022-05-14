from flask import Blueprint, render_template
from flask_login import login_required, current_user

# 建立(註冊)路由的函式

RoomRoutes = Blueprint('RoomRoutes', __name__, template_folder="templates", static_folder="static")
# 預設聊天室 -> 大家第一次登入後所擁有的聊天室(global，也就是大廳;): 不做聊天存儲
ROOMS = ["global", "users"]


@RoomRoutes.route('/index', methods=['GET'])
# @login_required
def index():
    return render_template('chat.html', username=current_user.Account, rooms=ROOMS)


@RoomRoutes.route('/getMemberList', methods=['GET'])
def get_member_list():
    # test data
    # future implementation must follow the JSON format
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
