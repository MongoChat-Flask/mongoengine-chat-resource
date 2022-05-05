# Flask-App config
from flask import Flask
from flask_bootstrap import Bootstrap
from app.config import *
# Routes modules
from chatroom.routes import RoomRoutes
from message.routes import MsgRoutes
from user.routes import UserRoutes

app = Flask(__name__)
app.config.from_object(Config)

# 註冊新的擴充路由
app.register_blueprint(UserRoutes, url_prefix="/user/")
app.register_blueprint(MsgRoutes, url_prefix="/msg/")
app.register_blueprint(RoomRoutes, url_prefix="/chat-r/")
# 啟動Bootstrap
Bootstrap(app)
