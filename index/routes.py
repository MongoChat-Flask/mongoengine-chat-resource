from flask import render_template, Blueprint

IndexRoutes = Blueprint('IndexRoutes', __name__)


# 按间距中的绿色按钮以运行脚本。
@IndexRoutes.route('')
def index():
    return render_template('index.html', login=True, success=False, activate=-1)
