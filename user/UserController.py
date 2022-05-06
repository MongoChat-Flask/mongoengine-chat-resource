import mongoengine
# 不能刪! 此行做為連接 Mongodb Atlas
import flask
from flask import Response, redirect, url_for, session, flash
from user.methods.config import *
from app import db
from user.methods.VerfiedEmail import establish_mail_object, check_url, send
from user.models import Users

assert isinstance(db, object)


# (Password)加密、解密之用途
# link:https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#customizing-the-configuration
# from passlib.hash import pbkdf2_sha256


def to_json(self) -> dict:
    return {
        "Account": self.Account,
        "Email": self.Email,
        "Password": self.Password,
        "Friends": self.Friends,
        "ChatRooms": self.ChatRooms,
    }


def CreateUser(account: str, email: str, password: bytes) -> "flask.Response":
    """這裡要添加<輸入參數>，以新增 'users' collection 的資料(帳號註冊功能)"""
    session["signal"] = {"login": True, "getinfo": True, "message": ""}
    try:
        user = Users(Account=account, Email=email, Password=password, Friends=[], ChatRooms=[])
        user.save()
        if Users.objects(Account=user.Account):
            msgObj = establish_mail_object(user.Email)
            # 送出驗證郵件(Gmail)
            flash('恭喜! 現在去接收郵件激活帳號吧!', category='success')
            return send(msgObj)
        else:
            session["signal"]["message"] = Message["Error_msg1"]
            return redirect(url_for('UserRoutes.sec'))
    # 針對各種例外情形產生response(error)，以給予相應的處理
    except mongoengine.errors.NotUniqueError:
        session["signal"]["message"] = Message["Error_msg2"]
        return redirect(url_for('UserRoutes.sec'))
    except mongoengine.errors.ValidationError:
        session["signal"]["message"] = Message["Error_msg3"]
        return redirect(url_for('UserRoutes.sec'))


def CheckUser(token, random) -> str | Response:
    """Activate = (重新導引至登入頁面並通知成功及接續步驟) ? (若為有效電子郵件) : (重新導引至登入頁面並通知失敗原因)"""
    session["signal"] = {"login": True, "getinfo": True, "message": ""}
    email = check_url(token, random)
    print(email)
    if not email == "":
        if Users.objects(Email=email).update(upsert=True, EmailVaildated=True) == 1:
            print(email)
            # 將更動其創建好的帳號進行更新狀態以激活
            session["signal"]["message"] = Message["Activate-success"]
            return redirect(url_for('UserRoutes.sec'))
        else:
            session["signal"]["message"] = Message["Error_msg0"]
            return redirect(url_for('UserRoutes.sec'))
    else:
        session["signal"]["message"] = Message["Error_msg0"]
        return redirect(url_for('UserRoutes.sec'))


def LoginUser(email: str, password: str) -> str | Response:
    """login = (redirect_to聊天頁面) ? (有該帳號存在且經過驗證) : (重新導引至登入頁面並依狀況顯示其相應行為)"""

    return ""


def LogoutUser():
    """Logout = (redirect_to登入頁面)"""
    return ""


def EditUser():
    """Edit = (切至聊天頁面, 顯示成功通知懸浮窗) ? (編輯且提交成功) : (失敗、回推至初始狀態，redirect_to聊天頁面並顯示失敗通知)"""
    return ""


def DeleteUser(account: str, password: str):
    """Delete = (切至登入頁面) ? (成功刪除帳號) : (失敗?，可能為Bug，need修復)"""
    return ""


def PendingRequest_from_Friend():
    """PendingRequest = (Add Friend to list) ? (i allow[True]) : (i do not allow[False])"""
    return ""


def PendingRequest_from_Chatroom():
    """PendingRequest = (Add ChatRoom to list) ? (i allow[True]) : (i do not allow[False])"""
    return ""


def ReadUser():
    """ReadUser = (切至User資訊頁面並顯示) ? (成功讀取User) : (Error:可能為伺服器錯誤)"""
    return ""
