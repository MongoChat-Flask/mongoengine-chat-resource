from flask import Blueprint

from user.UserController import CreateUser

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

