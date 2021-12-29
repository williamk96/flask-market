from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email = EmailField(label='Ex: emailaddress@domain.tld')
    password1 = PasswordField(label='super strong password')
    password2 = PasswordField(label='retype super strong password')
    submit = SubmitField(label='Submit')