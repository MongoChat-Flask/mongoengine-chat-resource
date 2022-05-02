# 不能刪! 此行做為連接 Mongodb Atlas

from mongo.mongo_setup import db
import datetime

assert isinstance(db, object)

def send_message(sender_id: str, room_id: str, msg: str):
    pass
