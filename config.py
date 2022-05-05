# For the usage of development
import os.path

from mongo import DB_URI
from flask_login import LoginManager

login_manager = LoginManager()
debug = True


class Config(object):
    # SECRET_KEY
    SECRET_KEY = DB_URI
