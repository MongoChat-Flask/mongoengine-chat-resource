from datetime import datetime
from mongoengine import *


class Message(Document):
    from models.Users import Users
    Message_creator = ReferenceField(Users, reverse_delete_rule=DO_NOTHING, required=True)
    Context = StringField(required=False)
    Timestamp = DateTimeField(default=datetime.utcnow())

    # @classmethod
    # def find_by_Timestamp(cls, Timestamp):
    #     print(type(Timestamp))
    #     # raw_query = {'Timestamp': {'$gte': Timestamp}}
    #     # cls.objects().order_by('Timestamp')
    #     return cls.objects()
