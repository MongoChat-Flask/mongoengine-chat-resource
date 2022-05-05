from flask_login import UserMixin
# Database module
from mongoengine import *
# 不能刪! 此行做為連接 mongodb atlas cluster
from mongo import db


class Users(Document):
    """資料model命名方式: Users -> users [In mongodb atlas]"""
    Account = StringField(unique=True, required=True, min_length=9, max_length=20)
    Email = EmailField(unique=True, required=True)
    Password = StringField(required=True)
    Friends = ListField(ReferenceField('self', reverse_delete_rule=CASCADE))
    ChatRooms = ListField()
    EmailVaildated = BooleanField(default=False)


# @login_manager.user_loader
# def load_user(user_id):
#     return Users.objects(pk=user_id).first()
