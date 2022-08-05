# Flask-App configstart
import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
# 登錄管理員
from flask_login import LoginManager
# Routes modules
from routes.ChatRoutes import RoomRoutes
from routes.MsgRoutes import MsgRoutes
from routes.UserRoutes import UserRoutes
# MongoDB
from mongoengine import connect
# SocketIO
from flask_socketio import SocketIO

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
# 啟動Bootstrap
Bootstrap(app)
db = connect(db="chat", host=os.environ.get('DB_URI'))
# db = connect(db="chat", host=DB_URI)
bcrypt = Bcrypt(app)
socketio = SocketIO(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'UserRoutes.login'
login_manager.login_message = '你必須登入才能存取該資源'
login_manager.login_message_category = 'info'

# 註冊新的擴充路由
app.register_blueprint(UserRoutes, url_prefix="/user/")
app.register_blueprint(MsgRoutes, url_prefix="/msg/")
app.register_blueprint(RoomRoutes, url_prefix="/chat-r/")
