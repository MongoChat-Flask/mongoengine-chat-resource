from flask import Blueprint, render_template

# 建立(註冊)路由的函式
RoomRoutes = Blueprint('RoomRoutes', __name__, template_folder="templates", static_folder="static")


@RoomRoutes.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('MainPage.html')


@RoomRoutes.route('/create', methods=['GET', 'POST'])
def create():
    return "create_chat_room()"


@RoomRoutes.route('/rename', methods=['GET', 'POST'])
def rename():
    return "rename_chat_room()"


@RoomRoutes.route('/delete', methods=['GET', 'POST'])
def delete():
    return "delete_chat_room()"


@RoomRoutes.route('/addMember', methods=['GET', 'POST'])
def add_member():
    return "chat_room_add_member()"


@RoomRoutes.route('/removeMember', methods=['GET', 'POST'])
def remove_member():
    return "chat_room_remove_member()"


@RoomRoutes.route('/getMemberList', methods=['GET'])
def get_member_list():
    return "get_member_list()"
