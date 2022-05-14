from mongoengine import *
from datetime import datetime


class Message(Document):
    from models.ChatRoom import ChatRoom
    Room_id = ReferenceField(ChatRoom, reverse_delete_rule=CASCADE, required=True)
    from models.Users import Users
    Message_creator = ReferenceField(Users, reverse_delete_rule=DO_NOTHING, required=True)
    Context = StringField(required=True)
    Timestamp = DateTimeField(default=datetime.utcnow)
