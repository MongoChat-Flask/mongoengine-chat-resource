from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RgisterForm(FlaskForm):
    """資料 網頁輸入表格 定義方式 [In html-form]"""
    account = StringField('Nickname', validators=[DataRequired(), Length(min=9, max=20)])
    email = StringField('Email address', validators=[DataRequired(), Email(), Length(min=9, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    """資料 網頁輸入表格 定義方式 [In html-form]"""
    email = StringField('Email address', validators=[DataRequired(), Email(), Length(min=9, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    submit = SubmitField('log in')
