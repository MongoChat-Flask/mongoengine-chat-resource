# flask-login module
from flask_login import UserMixin
# Database module
from mongoengine import *
from app import db, login_manager

assert isinstance(db, object)


@login_manager.user_loader
def load_user(user_id):
    return Users.objects(id=user_id).first()


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
        return cls.objects(Account=Account).all_fields().first()

    @classmethod
    def find_by_id(cls, pk) -> "Users":
        return cls.objects(pk=pk).all_fields().first()

    @classmethod
    def find_by_Email(cls, Email) -> "Users":
        return cls.objects(Email=Email).all_fields().first()

    @classmethod
    def hash_password(cls, password):
        from app import bcrypt
        return bcrypt.generate_password_hash(password)

    def match_password(self, password):
        from app import bcrypt
        return bcrypt.check_password_hash(self.Password, password)

    def __repr__(self):
        return '<User %r>' % self.Account
