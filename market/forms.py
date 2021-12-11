from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import EmailField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label='User Name')
    email = EmailField(label='Email')
    password1 = PasswordField(label='Enter password')
    password2 = PasswordField(label='Confirm password')
    submit = SubmitField(label='Submit')