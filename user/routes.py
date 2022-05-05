from flask import Blueprint, request, render_template
from user.UserController import *
from user import LoginForm, RgisterForm

# 建立(註冊)路由的函式
UserRoutes = Blueprint('UserRoutes', __name__)


# 註冊
@UserRoutes.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RgisterForm()
    if form.validate_on_submit():
        data = request.values.to_dict()
        print(data)
        return CreateUser(data['account'], data['email'], data['password'])
    else:
        if request.method == "GET":
            return render_template('index.html', login=False, form=form)
        else:
            session["signal"] = {
                "login": True,
                "getinfo": True,
                "message": ""
            }
            session["signal"]["message"] = Message["Error_msg3"]
            return redirect(url_for('IndexRoutes.sec'))


# 電子郵件認證
@UserRoutes.route('/vaild/confirm/', methods=['POST'])
def Activate_account():
    data = request.values.to_dict()
    return CheckUser(data['token'], data['random'])


# 登入
@UserRoutes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        data = request.values.to_dict()
        print(data)
        return LoginUser(email=data['email'], password=data['password'])
    else:
        if request.method == "GET":
            return render_template('index.html', login=True, form=form)
        else:
            session["signal"] = {
                "login": True,
                "getinfo": True,
                "message": ""
            }
            session["signal"]["message"] = Message["Error_msg3"]
            return redirect(url_for('IndexRoutes.sec'))


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
