from flask import Blueprint

# 建立(註冊)路由的函式
MsgRoutes = Blueprint('MsgRoutes', __name__)


@MsgRoutes.route('/send', methods=['POST'])
def send():
    return "send_message()"
