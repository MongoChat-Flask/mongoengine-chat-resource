from flask import Blueprint, request, render_template
from flask_login import login_user, current_user, logout_user
from Controllers.UserController import *
from models.form import LoginForm, RgisterForm

# 建立(註冊)路由的函式

UserRoutes = Blueprint('UserRoutes', __name__, template_folder="templates", static_folder="static")

print(UserRoutes.root_path)


# 按间距中的绿色按钮以运行脚本。
@UserRoutes.route('', methods=['GET'], endpoint='start')
@UserRoutes.route('/index', methods=['GET'], endpoint='sec')
def index():
    if "signal" in session:
        report = session["signal"]
        if type(report) is not dict:
            session.clear()
            return redirect(url_for('start'))
        if 'index' in request.path:  # endpoint='sec'
            session.clear()
            form = LoginForm() if report['login'] else RgisterForm()
            return render_template('index.html', login=report['login'], form=form, getinfo=report['getinfo'],
                                   message=report['message'])
        else:
            return render_template('index.html', login=True, form=LoginForm())
    return render_template('index.html', login=True, form=LoginForm())


# 註冊
@UserRoutes.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        # 判斷當前user狀態
        return redirect(url_for('ChatRoutes.index'))
    form = RgisterForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        from models.Users import Users
        pw_hash = Users.hash_password(password=form.Password.data)
        return CreateUser(account=form.Account.data, email=form.Email.data,
                          password=pw_hash)
    else:
        return render_template('index.html', login=False, form=form)


# 電子郵件認證
@UserRoutes.route('/vaild/confirm/', methods=['POST'])
def Activate_account():
    data = request.values.to_dict()
    return CheckUser(data['token'], data['random'])


# 登入
@UserRoutes.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        # 判斷當前user狀態
        return redirect(url_for('ChatRoutes.index'))
    form = LoginForm()
    if form.validate_on_submit():
        from models.Users import Users
        email = form.Email.data
        pwd = form.Password.data
        remember = form.Remember.data
        user = Users.find_by_Email(email)
        print(user)  # and user.Online
        if user and user.match_password(password=pwd):
            login_user(user=user, remember=remember)
            flash('You were successfully logged in', category='success')
            # next=...
            if request.args.get('next'):
                next_page = request.args.get('next')
                return redirect(url_for(next_page))
            return redirect(url_for('RoomRoutes.index'))
        else:
            session["signal"] = {"login": True, "getinfo": True,
                                 "message": Message["Error_msg4"].format(form.Email.data)}
            return redirect(url_for('UserRoutes.sec'))
    else:
        return render_template('index.html', login=True, form=form)


# 登出
@UserRoutes.route('/logout', methods=['GET'])
def logout():  # 使用者註冊
    logout_user()
    return redirect(url_for('UserRoutes.login'))


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
