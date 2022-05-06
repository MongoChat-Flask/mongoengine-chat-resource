# 不能刪! 此行做為連接 Mongodb Atlas

from app import db
import flask
from models import User as Users

assert isinstance(db, object)


def create_chat_room(room_name: str) -> "flask.Response":
    """create new chat room with room_name"""
    pass


def rename_chat_room(room_id: str, new_name: str) -> "flask.Response":
    """rename chat room with room_id and new_name"""
    pass


def delete_chat_room(room_id: str) -> "flask.Response":
    """delete chat room by id"""
    pass


def chat_room_add_member(room_id: str, user_id: str) -> "flask.Response":
    pass


def chat_room_remove_member(room_id: str, user_id: str) -> "flask.Response":
    pass


def get_member_list(room_id: str) -> list[Users]:
    """get all member of a chat room"""
    pass
