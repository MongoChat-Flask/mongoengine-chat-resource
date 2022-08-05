# 不能刪! 此行做為連接 Mongodb Atlas

import config

assert isinstance(config.db, object)


def send_message(sender_id: str, room_id: str, msg: str):
    pass
