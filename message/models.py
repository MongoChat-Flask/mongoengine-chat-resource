from mongoengine import *
from user.models import Users
from chatroom.models import ChatRoom
from datetime import datetime


class Message(Document):
    Room_id = ReferenceField(ChatRoom, reverse_delete_rule=CASCADE, required=True)
    Message_creator = ReferenceField(Users, reverse_delete_rule=DO_NOTHING, required=True)
    Context = StringField(required=True)
    Timestamp = DateTimeField(default=datetime.utcnow)