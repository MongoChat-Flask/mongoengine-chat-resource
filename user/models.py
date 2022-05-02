# Database module
from mongoengine import *
# 不能刪! 此行做為連接 mongodb atlas cluster
from mongo import db


class Users(Document):
    """資料model命名方式: Users -> users [In mongodb atlas]"""
    Account = StringField(unique=True, required=True, min_length=9, max_length=20)
    Email = EmailField(unique=True, required=True)
    Password = StringField(required=True, max_length=20, min_length=8)
    Friends = ListField(ReferenceField('self', reverse_delete_rule=CASCADE))
    ChatRooms = ListField()
    EmailVaildated = BooleanField(default=False)
