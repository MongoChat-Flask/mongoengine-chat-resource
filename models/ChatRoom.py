from mongoengine import *
import Users


class ChatRoom(Document):
    Room_name = StringField(required=True)
    Member_list = ListField(ReferenceField(Users), reverse_delete_rule=CASCADE)
