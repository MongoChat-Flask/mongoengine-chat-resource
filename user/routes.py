from flask import Blueprint, request, render_template
from user.UserController import *
from user import LoginForm, RgisterForm

# 建立(註冊)路由的函式
UserRoutes = Blueprint('UserRoutes', __name__)


# 註冊
@UserRoutes.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template('index.html', login=False, form=RgisterForm())
    # request.method == "POST"
    data = request.values.to_dict()
    return CreateUser(data['account'], data['email'], data['password'])


# 電子郵件認證
@UserRoutes.route('/vaild/confirm/', methods=['POST'])
def Activate_account():
    data = request.values.to_dict()
    return CheckUser(data['token'], data['random'])


# 登入
@UserRoutes.route('/login', methods=['GET', 'POST'])
def login():
    return "LoginUser()"


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
