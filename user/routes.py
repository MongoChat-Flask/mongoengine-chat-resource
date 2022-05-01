import itsdangerous
from flask import Blueprint

from user.UserController import *

# 建立(註冊)路由的函式
UserRoutes = Blueprint('UserRoutes', __name__)


@UserRoutes.route('/signup', methods=['GET'])
def signup():  # 使用者註冊
    return CreateUser()


@UserRoutes.route('/login', methods=['GET'])
def login():  # 使用者註冊
    return "VaildateUser()"


@UserRoutes.route('/logout', methods=['GET'])
def logout():  # 使用者註冊
    return "LogoutUser()"


@UserRoutes.route('/info', methods=['GET'])
def info():
    return "InfoUser()"


@UserRoutes.route('/edit', methods=['GET'])
def edit():
    return "EditUser()"


@UserRoutes.route('/delete', methods=['GET'])
def delete():
    return "DeleteUser()"


@UserRoutes.route('/sendtest', methods=['GET', 'POST'])
def vaildation():
    return Send_for_Activate()


@UserRoutes.route('/sendtest/confirm/<token>', methods=['GET'])
def Activate_account(token):
    try:
        email_from_url = s.loads(token, salt='MongoChat-Activate', max_age=60)
        return "你的帳戶已激活!"
    except itsdangerous.exc.SignatureExpired:
        return "該連結已過期，請重新註冊!"
