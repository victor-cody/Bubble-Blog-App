from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, Email 



class RegistrationForm(FlaskForm):
    """
    Our Registration Form Class
    """
    # Username Field
    username = StringField(
    'Usename',
    validators=[DataRequired(message="choose your username"), 
    Length(min=5, max=12)],
    description="Your Username")
    # Email Field
    email = StringField(
        'Email Address',
        validators=[DataRequired(message="please fill in your email address"), 
        Email()],
        description="Your Email Address",)
    # Password Field
    password = PasswordField(
    'Password',
    validators=[DataRequired(message="your password"),
    Length(
        min=6, max=12, message='Your password must be a minimum of 6 - 12 charaters'),
    EqualTo('confirm_password', message='Your Passwords must match')])
    # Password Confirmation Field
    confirm_password = PasswordField(
        'Repeat Password',
        validators=[DataRequired(message="confirm password"),
        EqualTo('password', message='Your Passwords must match')])
    remember = BooleanField('Remember Me',default='checked')
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    """
    Our Login Form Class To Login the user
    """
    # Email Field
    email = StringField(
        'Email Address',
        validators=[DataRequired(message="fill in your email address"), Email()],
        description="Your Email Address")
    # Password Field
    password = PasswordField(
    'New Password',
    validators=[DataRequired(message="your password"),
    Length(min=6, max=12, message='Your password must be a minimum of 6 - 12 charaters')])
    remember = BooleanField('Remember Me',default='checked')
    submit = SubmitField('Log In')
