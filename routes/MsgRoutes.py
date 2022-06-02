from flask import Blueprint, request

# 建立(註冊)路由的函式
MsgRoutes = Blueprint('MsgRoutes', __name__)


@MsgRoutes.route('/send', methods=['POST'])
def send():
    m = request.form["msg"]
    print(m)
    msgs["msgs"].append(m)
    return "<script>window.location='/chat-r/index'</script>"


@MsgRoutes.route('/get', methods=['GET'])
def get():
    # must follow json format
    # return '{"msgs": ["hi", "hello", "how", "he", "hand", "hover", "human"]}'
    return json.dumps(msgs)








import json
msgs = {"msgs": ["hi", "hello", "how", "he", "hand", "hover", "human"]}
