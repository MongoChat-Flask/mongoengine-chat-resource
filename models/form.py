from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError




class RgisterForm(FlaskForm):
    """資料 網頁輸入表格 定義方式 [In html-form]"""
    Account = StringField('Nickname',
                          validators=[InputRequired(message="Enter Your Name Please"), Length(min=9, max=20)])
    Email = StringField('Email Address',
                        validators=[InputRequired(message="Enter Email Please"), Email()])
    Password = PasswordField('Password',
                             validators=[InputRequired(message="Enter Password Please"), Length(min=8, max=50)])
    confirm = PasswordField('Repeat Password',
                            validators=[InputRequired(), EqualTo('Password', message='123')])
    submit = SubmitField('Sign Up')

    def validate_Account(self, Account):
        from models.User import Users
        account = Users.objects(Account=Account.data).count()
        print(account)
        if account != 0:
            raise ValidationError(message='Your Name already token')

    def validate_Email(self, Email):
        from models.User import Users
        email = Users.objects(Email=Email.data).count()
        print(email)
        if email != 0:
            raise ValidationError('Your Email already token')


class LoginForm(FlaskForm):
    """資料 網頁輸入表格 定義方式 [In html-form]"""
    Email = StringField('Email address', validators=[InputRequired(), Email()])
    Password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=50)])
    submit = SubmitField('log In')

    def validate_Email(self, Email):
        from models.User import Users
        email = Users.objects(Email=Email.data).count()
        if email != 1:
            raise ValidationError(message='Your Email is not exists')
