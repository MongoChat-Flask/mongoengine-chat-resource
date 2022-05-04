# For the usage of development
import os.path

from mongo import DB_URI

debug = True


class Config(object):
    # SECRET_KEY
    SECRET_KEY = DB_URI
