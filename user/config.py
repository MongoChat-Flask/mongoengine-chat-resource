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
    "Sign-up-success": "Success! 檢查電子郵件以激活帳戶",
    "Activate-success": "Success! 可以登入了!",
    "Error_msg0": "Error! 好像出現甚麼錯誤!",
    "Error_msg1": "Error! 請重來一次!",
    "Error_msg2": "Error! 你註冊的部分資訊已被使用!",
    "Error_msg3": "Error! 請確認你輸入的資訊無誤!",
    "Error_msg4": "Error! 郵箱不存在或是密碼不匹配！",
}
