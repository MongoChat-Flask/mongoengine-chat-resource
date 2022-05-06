# Flask-App config
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app.config import *
# Routes modules
from routes.ChatRoutes import RoomRoutes
from routes.MsgRoutes import MsgRoutes
from routes.UserRoutes import UserRoutes
# Mongoengine
from mongoengine import connect

app = Flask(__name__)
app.config.from_object(Config)

# 註冊新的擴充路由
app.register_blueprint(UserRoutes, url_prefix="/user/")
app.register_blueprint(MsgRoutes, url_prefix="/msg/")
app.register_blueprint(RoomRoutes, url_prefix="/chat-r/")
# 啟動Bootstrap
Bootstrap(app)
db = connect(db="chat", host=DB_URI)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'UserRoutes.index'
login_manager.login_message = '你必須登入才能存取該資源'
login_manager.login_message_category = 'info'
