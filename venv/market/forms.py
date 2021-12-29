from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import Users

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = Users.query.filter_by(username=username_to_check).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username.')

    def validate_email(self, email_to_check)
        email = Users.query.filter_by(email=email_to_check).first()
        if email:
            raise ValidationError('Email address already exists! Please try a different email address.')

    username = StringField(label='username', validators=[Length(min=2, max=30), DataRequired()])
    email = EmailField(label='email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='super strong password', validators=[Length(min=12), DataRequired()])
    password2 = PasswordField(label='retype super strong password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')