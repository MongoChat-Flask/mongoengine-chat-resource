from itsdangerous import URLSafeTimedSerializer

gacc = 'monogchatoffical@gmail.com'
gpwd = 'nwumxozrxzltgomt'
secret_key = 'vrb65!v&817v*712lk]brene@'
s = URLSafeTimedSerializer(secret_key=secret_key)
vertification_context = "<h4>" \
                        "😁你好，我是MongoChat官方維護人員，為你附上連結，以激活你的帳號及其功能" \
                        "<form action='http://localhost:5000/user/vaild/confirm/' " \
                        "target='_blank' method='POST'>" \
                        "<input type='hidden' name='random' value='{}'>" \
                        "<input type='hidden' name='token' value='{}'>" \
                        "<button type='submit' name='button'>激活</button>" \
                        "</form><br>" \
                        "若你是不知情的狀況下收到該封Email，可以略過或是刪除。<br><br><br><br>" \
                        "<br><br><br><br>" \
                        "請支持辛苦的燒肝工程師團隊!! 感謝支持!!" \
                        "</h4>"
# action = 'url' ->需要改為(部署階段)的鏈接
Message = {
    "Sign-up-success": "檢查電子郵件以激活帳戶",
    "Activate-success": "已激活! 可以登入了!",
    "Error": "Error!<br>好像出現甚麼錯誤!",
}