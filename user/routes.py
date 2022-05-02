from flask import Blueprint
from user.UserController import *

# 建立(註冊)路由的函式
UserRoutes = Blueprint('UserRoutes', __name__)


# 註冊
@UserRoutes.route('/signup', methods=['GET'])
def signup():
    return CreateUser()


# 電子郵件認證
@UserRoutes.route('/vaild/confirm/', methods=['GET', 'POST'])
def Activate_account():
    return CheckUser(request.values.get('token'), request.values.get('random'))


# 登入
@UserRoutes.route('/login', methods=['GET'])
def login():
    return "VaildateUser()"


# 登出
@UserRoutes.route('/logout', methods=['GET'])
def logout():  # 使用者註冊
    return "LogoutUser()"


# 讀取資訊
@UserRoutes.route('/info', methods=['GET'])
def info():
    return "InfoUser()"


# 編輯
@UserRoutes.route('/edit', methods=['GET'])
def edit():
    return "EditUser()"


# 刪除
@UserRoutes.route('/delete', methods=['GET'])
def delete():
    return "DeleteUser()"
