# flask-mongoengine config
mongo_password = "42067423"
db = "chat"
username = "wc2014920"
DB_URI = "mongodb+srv://{}:{}@mongochat.r6o8d.mongodb.net/{}?" \
         "retryWrites=true&w=majority".format(username, mongo_password, db)


class Config(object):
    # SECRET_KEY
    SECRET_KEY = DB_URI
