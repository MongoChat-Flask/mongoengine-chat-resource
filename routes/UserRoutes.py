from flask import Blueprint, request, render_template
from flask_login import login_user, current_user, logout_user, login_required
from Controllers.UserController import *
from models.form import LoginForm, RgisterForm

# 建立(註冊)路由的函式

UserRoutes = Blueprint('UserRoutes', __name__, template_folder="templates", static_folder="static")

print(UserRoutes.root_path)


@UserRoutes.route('/1', methods=['GET'])
def test():
    return render_template('chat.html')


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
        # 若 user 成功登入 -> 更新時間: LoginAt、LogoutAt (第一次為相同)
        if user and user.match_password(password=pwd):
            login_user(user=user, remember=remember)
            # flash('You were successfully logged in', category='success')
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
@login_required
def logout():  # 使用者註冊
    logout_user()
    flash('You were successfully logged out', category='success')
    return redirect(url_for('UserRoutes.login'))


# 讀取資訊
@UserRoutes.route('/info', methods=['GET'])
@login_required
def info():
    return "InfoUser()"


# 讀取聊天室名單
@UserRoutes.route('/chat_room_list', methods=['GET'])
#@login_required
def chat_room_list():
    # must follow JSON format
    return '{"_id":["1","2","4","5"]}'


# 編輯
@UserRoutes.route('/edit', methods=['GET'])
@login_required
def edit():
    return "EditUser()"


# 刪除
@UserRoutes.route('/delete', methods=['GET'])
@login_required
def delete():
    delete_Account = current_user.Account
    from models.Users import Users
    user = Users.objects(Account=delete_Account).first()
    user.delete()
    if Users.objects(Account=delete_Account).count() == 0:
        logout_user()
        flash('Success! Account already deleted!', category='success')
        return redirect(url_for('UserRoutes.login'))
    else:
        flash('Error! Can not delete your Account!', category='danger')
        return redirect(url_for('ChatRoutes.index'))
