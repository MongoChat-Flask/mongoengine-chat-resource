from mongoengine import Document, ReferenceField, StringField, DateTimeField, BinaryField, DO_NOTHING, CASCADE
from datetime import datetime


class Message(Document):
    from models.ChatRoom import ChatRoom
    Room_name = StringField(ReferenceField(ChatRoom, reverse_delete_rule=CASCADE, required=True))
    from models.Users import Users
    Message_creator = ReferenceField(Users, reverse_delete_rule=DO_NOTHING, required=True)
    Context = StringField(required=False)
    Image = BinaryField(required=False)
    Video_url = StringField(required=False)
    Timestamp = DateTimeField(default=datetime.utcnow)
