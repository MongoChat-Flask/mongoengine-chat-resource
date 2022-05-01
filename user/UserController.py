from config import vertification_context, gacc, gpwd, secret_key
from itsdangerous import URLSafeTimedSerializer
# 不能刪! 此行做為連接 Mongodb Atlas
from flask import jsonify, request
from mongo.mongo_setup import db
from user.models import Users
import email.message
import mongoengine
import smtplib

assert isinstance(db, object)

s = URLSafeTimedSerializer(secret_key=secret_key)


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


def CheckUser():  # login = (redirect_to聊天頁面) ? (有該帳號存在且經過驗證) : (重新導引至登入頁面並依狀況顯示其相應行為)
    return ""


def Send_for_Activate():  # vaildation = (redirect_to登入頁面) ? (點選其電子連結，通過驗證) : (超時，刪除過期註冊帳號)
    if request.method == 'GET':
        return '<form action="/user/sendtest" method="POST">' \
               '<input name="email">' \
               '<input type="submit"></form>'
    email_not_verified = request.form['email']
    token = s.dumps(email_not_verified, salt='MongoChat-Activate')

    # return 'The email you entered is {}, and the token is {}'.format(request.form['email'], token)

    # 建立訊息物件
    msg = email.message.EmailMessage()
    msg["Form"] = gacc
    msg["To"] = "xz20201222@gmail.com"  # 這裏會被輸入參數取代
    msg["Subject"] = "MongoChat - 郵件認證"
    msg.add_alternative(vertification_context.format(token), subtype="html")
    # 連線到SMTP Sevver
    try:
        # 可以從網路上找到主機名稱和連線埠
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # 建立gmail連線
        server.login(gacc, gpwd)
        server.send_message(msg)
        server.close()  # 發送完成後關閉連線
        print("Send Complete!")
        return jsonify({
            "HTTP": 200,
            "message": "成功送出"

        })
    except Exception as e:
        print("Error message", e)
        return jsonify({
            "HTTP": 201,
            "message": str(e)
        })


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
