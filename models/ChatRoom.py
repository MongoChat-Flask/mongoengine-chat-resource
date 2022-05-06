from mongoengine import *
import User


class ChatRoom(Document):
    Room_name = StringField(required=True)
    Room_creator = ReferenceField(User, reverse_delete_rule=CASCADE)
    Member_list = ListField(ReferenceField(User), reverse_delete_rule=CASCADE)