# Flask-App config
import os
from flask import Flask, session
from flask_bootstrap import Bootstrap

from chatroom.routes import RoomRoutes
from config import *
# Routes modules
from index.routes import IndexRoutes
from message.routes import MsgRoutes
from user.routes import UserRoutes

app = Flask(__name__)
app.config.from_object(Config)

# 註冊新的擴充路由
app.register_blueprint(IndexRoutes, url_prefix="/")
app.register_blueprint(UserRoutes, url_prefix="/user/")
app.register_blueprint(MsgRoutes, url_prefix="/msg/")
app.register_blueprint(RoomRoutes, url_prefix="/chat-r/")
# 啟動Bootstrap
Bootstrap(app)
if __name__ == '__main__':
    app.run(debug=debug)
