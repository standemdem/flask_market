from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username = username_to_check.data).first()
        if user:
            raise ValidationError(f'{username_to_check.data} already exists, please try a diferent user name')

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email = email_to_check.data).first()
        if email:
            raise ValidationError(f'{email_to_check.data} already exists, please pick another one')

    username = StringField(label='User Name', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Enter password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Submit')

class LoginForm(FlaskForm):
    username = StringField(label='User name', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')