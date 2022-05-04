import ast
from flask import render_template, Blueprint, session
from user import LoginForm

IndexRoutes = Blueprint('IndexRoutes', __name__)


# 按间距中的绿色按钮以运行脚本。
@IndexRoutes.route('/', methods=['GET'])
def index():
    if "signal" in session:
        print(f"session:{session['signal']}")
        report = session['signal']
        session.clear()
        return render_template('index.html',
                               login=True, form=LoginForm(),
                               getinfo=report['getinfo'], message=report['message'])
    return render_template('index.html',
                           login=True, form=LoginForm(),
                           getinfo=False)
