# 不能刪! 此行做為連接 Mongodb Atlas
from mongo.mongo_setup import db
from user.models import Users
from flask import jsonify
import mongoengine
assert isinstance(db, object)


# (Password)加密、解密之用途
# link:https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#customizing-the-configuration
# from passlib.hash import pbkdf2_sha256

def to_json(self):
    return {
        "Account": self.Account,
        "Email": self.Email,
        "Password": self.Password,
        "Friends": self.Friends,
        "ChatRooms": self.ChatRooms,
    }


def CreateUser():  # 這裡要添加<輸入參數>，以新增 'users' collection 的資料(帳號註冊功能)

    try:
        user = Users(
            Account="wc22014920",
            Email="wc201920@gmail.com",
            Password="42067423",
            Friends=[],
            ChatRooms=[],
        )
        user.save()
        if Users.objects(Account=user.Account):
            return jsonify(to_json(user)), 200
        else:
            return jsonify({
                "Error_msg": "註冊失敗! Please try again!",
                "HTTP": 333
            }), 201
    except mongoengine.errors.NotUniqueError:  # 針對各種例外情形產生response(error)，以給予相應的處理
        return jsonify({
            "Error_msg": "你註冊的部分資訊已被使用!",
            "HTTP": 222
        }), 201
    except mongoengine.errors.ValidationError:
        return jsonify({
            "Error_msg": "請確認你輸入的資訊無誤!",
            "HTTP": 111
        }), 203
