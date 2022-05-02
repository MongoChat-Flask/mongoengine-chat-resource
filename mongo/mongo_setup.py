from mongoengine import connect
from mongo.config import *
db = connect(db='chat', host=DB_URI)
