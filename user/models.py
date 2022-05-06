# flask-login module
from flask_login import UserMixin
# Database module
from mongoengine import *
from app import db, login_manager

assert isinstance(db, object)


@login_manager.user_loader
def load_user(user_id):
    return Users.get(user_id)


class Users(Document, UserMixin):
    """資料model命名方式: Users -> users [In mongodb atlas]"""
    Account = StringField(unique=True, required=True, min_length=9, max_length=20)
    Email = EmailField(unique=True, required=True)
    Password = BinaryField(required=True)
    Friends = ListField(ReferenceField('self', reverse_delete_rule=CASCADE))
    ChatRooms = ListField()
    EmailVaildated = BooleanField(default=False)
    Online = BooleanField(default=False)

    @classmethod
    def find_by_Account(cls, Account) -> "Users":
        return cls.objects(Account=Account).first()

    @classmethod
    def find_by_id(cls, pk) -> "Users":
        return cls.objects(pk=pk).first()

    @classmethod
    def find_by_Email(cls, Email) -> "Users":
        return cls.objects(Email=Email).first()

    @classmethod
    def hash_password(cls, password, bcrypt):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")

    def match_password(self, password, bcrypt):
        return bcrypt.checkpw(password.encode('utf-8'), self.Password.encode("utf-8"))

    def __repr__(self):
        return '<User %r>' % self.Account
