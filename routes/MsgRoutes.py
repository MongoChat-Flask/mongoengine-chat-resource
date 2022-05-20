from flask import Blueprint

# 建立(註冊)路由的函式
MsgRoutes = Blueprint('MsgRoutes', __name__)


@MsgRoutes.route('/send', methods=['POST'])
def send():
    return "send_message()"


@MsgRoutes.route('/get', methods=['GET'])
def get():
    # must follow json format
    return '{"msgs": ["hi", "hello", "how", "he", "hand", "hover", "human"]}'
