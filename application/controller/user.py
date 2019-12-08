from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from application.handler import user as user_handler


class RegisterForm(FlaskForm):
    username = StringField('用户名：', validators=[DataRequired(), Length(min=6, max=20)])
    password = PasswordField('密码：', validators=[DataRequired(), Length(min=6, max=16)])
    confirm = PasswordField('确认密码：', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('提交')

    def validate_username(self, username):
        if user_handler.query_user_exist(username=username.data):
            raise ValidationError("用户已存在。")


class UserForm(FlaskForm):
    username = StringField('用户名：', validators=[DataRequired(), Length(min=6, max=20)])
    password = PasswordField('密码：', validators=[DataRequired(), Length(min=6, max=16)])
    submit = SubmitField('提交')
