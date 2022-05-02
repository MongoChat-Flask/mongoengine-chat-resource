import mongoengine
# 不能刪! 此行做為連接 Mongodb Atlas
from flask import jsonify, request
from mongo.mongo_setup import db
from user.methods.VerfiedEmail import establish_mail_object, check_url, send
from user.models import Users

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
            EmailVaildated=False
        )
        user.save()
        if Users.objects(Account=user.Account):
            msgObj = establish_mail_object(user.Email)
            # 送出驗證郵件(Gmail)
            return send(msgObj)
        else:
            return jsonify({
                "Error_msg": "註冊失敗! Please try again!",
                "HTTP": 204
            }), 204
    except mongoengine.errors.NotUniqueError:  # 針對各種例外情形產生response(error)，以給予相應的處理
        return jsonify({
            "Error_msg": "你註冊的部分資訊已被使用!",
            "HTTP": 205
        }), 205
    except mongoengine.errors.ValidationError:
        return jsonify({
            "Error_msg": "請確認你輸入的資訊無誤!",
            "HTTP": 206
        }), 206


def CheckUser(token, random):  # Activate = (重新導引至登入頁面並通知成功及接續步驟) ? (若為有效電子郵件) : (重新導引至登入頁面並通知失敗原因)
    if check_url(token, random):
        return jsonify({
            "State": True
        }), 207
    else:
        return jsonify({
            "State": False
        }), 208


def LoginUser():  # login = (redirect_to聊天頁面) ? (有該帳號存在且經過驗證) : (重新導引至登入頁面並依狀況顯示其相應行為)
    return ""


def LogoutUser():  # Logout = (redirect_to登入頁面)
    return ""


def EditUser():  # Edit = (切至聊天頁面, 顯示成功通知懸浮窗) ? (編輯且提交成功) : (失敗、回推至初始狀態，redirect_to聊天頁面並顯示失敗通知)
    return ""


def DeleteUser():  # Delete = (切至登入頁面) ? (成功刪除帳號) : (失敗?，可能為Bug，need修復)
    return ""


def PendingRequest_from_Friend():
    # PendingRequest = (Add Friend to list) ? (i allow[True]) : (i do not allow[False])
    return ""


def PendingRequest_from_Chatroom():
    # PendingRequest = (Add ChatRoom to list) ? (i allow[True]) : (i do not allow[False])
    return ""


def ReadUser():
    # ReadUser = (切至User資訊頁面並顯示) ? (成功讀取User) : (Error:可能為伺服器錯誤)
    return ""
