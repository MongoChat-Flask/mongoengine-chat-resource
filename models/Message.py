from mongoengine import *
from models.ChatRoom import ChatRoom
from datetime import datetime

import Users


class Message(Document):
    Room_id = ReferenceField(ChatRoom, reverse_delete_rule=CASCADE, required=True)
    Message_creator = ReferenceField(User, reverse_delete_rule=DO_NOTHING, required=True)
    Context = StringField(required=True)
    Timestamp = DateTimeField(default=datetime.utcnow)
