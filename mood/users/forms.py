from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(FlaskForm):
    email = EmailField('Email', [DataRequired(), Length(min=4, max=256)])
    username = StringField('Username', [DataRequired(), Length(min=4, max=256)])
    password = PasswordField('Password', [DataRequired(), Length(min=4, max=256)])
    confirmation = PasswordField('Re-enter Password', [DataRequired(), Length(min=4, max=256), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = EmailField('Email', [DataRequired(), Length(min=4, max=256)])
    password = PasswordField('Password', [DataRequired(), Length(min=4, max=256)])
    submit = SubmitField('Login')
