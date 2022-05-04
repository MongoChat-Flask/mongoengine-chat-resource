from flask import render_template, Blueprint, session, request, url_for
from werkzeug.utils import redirect

from user import LoginForm

IndexRoutes = Blueprint('IndexRoutes', __name__)


# 按间距中的绿色按钮以运行脚本。
@IndexRoutes.route('', methods=['GET'], endpoint='start')
@IndexRoutes.route('/index', methods=['GET'], endpoint='sec')
def index():
    if "signal" in session:
        report = session["signal"]
        if type(report) is not dict:
            session.clear()
            print(request.path)
            return redirect(url_for('start'))
        print(request.path)
        if 'index' in request.path:
            session.clear()
            return render_template('index.html', login=report['login'], form=LoginForm(), getinfo=report['getinfo'], message=report['message'])
        else:
            # session.clear()
            return render_template('index.html', login=True, form=LoginForm())
    print(request.path)
    return render_template('index.html', login=True, form=LoginForm())
