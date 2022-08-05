import smtplib
import uuid
import email.message
from typing import Union

from flask import Response, redirect, url_for, session
from itsdangerous import SignatureExpired
from user.config import *
from flask_apscheduler import APScheduler
import datetime
import logging

# from configstart import db
# assert isinstance(db, object)


def deleteInvalidAccount(taskName, InvalidAccount):
    from models.Users import Users
    user = Users.objects(Email=InvalidAccount).first()
    if not user.EmailVaildated:
        user.delete()
        print("該帳號為非法用戶! 已確定刪除!\n")
    else:
        print("該帳號為合法用戶!\n")


def send(msgObj, id) -> Union[str, Response]:
    # 連線到 SMTP Server
    try:
        # 可以從網路上找到主機名稱和連線埠
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # 建立gmail連線
        server.login(msgObj[1], msgObj[2])
        server.send_message(msgObj[0])
        server.close()  # 發送完成後關閉連線
        from models.Users import Users
        user = Users.objects(Email=id).first()
        aps = APScheduler()
        aps.add_job(func=deleteInvalidAccount, args=('一次性任務', id),
                    next_run_time=datetime.datetime.now().astimezone() + datetime.timedelta(seconds=65),
                    timezone='Asia/Taipei', id=id)
        aps.start()
        logging.info("user.methods.VerifiedEmail.send: Send Complete!")
        session["signal"] = {"login": True, "getinfo": True, "message": Message["Sign-up-success"]}
        return redirect(url_for('UserRoutes.sec'))

    except Exception as err:
        logging.critical("unexpected error:", err)
        return redirect(url_for('UserRoutes.signup'))


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
        from models.Users import Users
        decrypt_mail = s.loads(token, salt='MongoChat-Activate-{}'.format(random_string), max_age=60)
        logging.info("user email count:", Users.objects(Email=decrypt_mail).count())
        return decrypt_mail if Users.objects(Email=decrypt_mail).count() == 1 else ""
    except SignatureExpired:
        logging.error("連結已過期，需重新註冊!")
        return ""
    except Exception as err:
        logging.critical("unexpected exception:", err)
        return ""
