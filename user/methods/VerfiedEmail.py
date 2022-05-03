import http
import smtplib
import uuid
import email.message

from flask import Response
from itsdangerous import SignatureExpired
from user.methods.config import *
from user.models import Users
from mongo import db
import flask
import logging

assert isinstance(db, object)


def send(msgObj) -> str | Response:
    # 連線到 SMTP Server
    try:
        # 可以從網路上找到主機名稱和連線埠
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # 建立gmail連線
        server.login(msgObj[1], msgObj[2])
        server.send_message(msgObj[0])
        server.close()  # 發送完成後關閉連線
        logging.info("user.methods.VerifiedEmail.send: Send Complete!")
        return flask.render_template('index.html', login=True, getinfo=True, message=Message["Sign-up-success"])

    except Exception as err:
        logging.critical("unexpected error:", err)
        return flask.render_template('index.html', login=False, getinfo=True, message=Message["Error"])


def establish_mail_object(email_not_verified) -> tuple:
    logging.info("user.methods.VerifiedEmail.establish_main_object:", email_not_verified)
    random_string = uuid.uuid4()
    token = s.dumps(email_not_verified, salt="MongoChat-Activate-{}".format(random_string))
    msg = email.message.EmailMessage()
    msg["Form"] = gacc
    msg["To"] = email_not_verified  # 這裏會被輸入參數取代
    msg["Subject"] = "MongoChat - 郵件認證"
    link = vertification_context.format(random_string, token)
    msg.add_alternative(link, subtype="html")
    return msg, gacc, gpwd


def check_url(token, random_string) -> str:
    try:
        decrypt_mail = s.loads(token, salt='MongoChat-Activate-{}'.format(random_string), max_age=60)
        logging.info("user email count:", Users.objects(Email=decrypt_mail).count())
        return decrypt_mail if Users.objects(Email=decrypt_mail).count() == 1 else ""
    except SignatureExpired:
        logging.error("連結已過期，需重新註冊!")
        return ""
    except Exception as err:
        logging.critical("unexpected exception:", err)
        return ""
