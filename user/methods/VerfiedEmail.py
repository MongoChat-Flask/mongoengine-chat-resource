import smtplib
import uuid
import email.message
from itsdangerous import SignatureExpired
from user.methods.config import *
from user.models import Users
from mongo.mongo_setup import db
from flask import jsonify

assert isinstance(db, object)


def send(msgObj):
    # 連線到 SMTP Server
    try:
        # 可以從網路上找到主機名稱和連線埠
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # 建立gmail連線
        server.login(msgObj[1], msgObj[2])
        server.send_message(msgObj[0])
        server.close()  # 發送完成後關閉連線
        print("Send Complete!")
        return jsonify({
            "HTTP": 200,
            "message": "成功送出"

        })
    except Exception:
        return jsonify({
            "HTTP": 201,
            "message": "非預期錯誤!"
        })


def establish_mail_object(email_not_verified):
    print(email_not_verified)
    random_string = uuid.uuid4()
    token = s.dumps(email_not_verified, salt='MongoChat-Activate{}'.format(random_string))
    msg = email.message.EmailMessage()
    msg["Form"] = gacc
    msg["To"] = email_not_verified  # 這裏會被輸入參數取代
    msg["Subject"] = "MongoChat - 郵件認證"
    link = vertification_context.format(random_string, token)
    msg.add_alternative(link, subtype="html")
    return msg, gacc, gpwd


def check_url(token, random_string):
    try:
        decrypt_mail = s.loads(token, salt='MongoChat-Activate{}'.format(random_string), max_age=60)
        print(Users.objects(Email=decrypt_mail).count())
        return True if 1 == Users.objects(Email=decrypt_mail).count() else False
    except SignatureExpired:
        print("該連結已過期，請重新註冊!")
        return False
