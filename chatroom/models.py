from mongoengine import *
from user.models import Users


class ChatRoom(Document):
    Room_name = StringField(required=True)
    Room_creator = ReferenceField(Users, reverse_delete_rule=CASCADE)
    Member_list = ListField(ReferenceField(Users), reverse_delete_rule=CASCADE)