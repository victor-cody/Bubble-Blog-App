from flask_wtf import FlaskForm
from wtforms import (BooleanField, PasswordField, SelectMultipleField, StringField, SubmitField, TextAreaField, ValidationError)
from wtforms.validators import DataRequired, Email, EqualTo, Length
from App import bcrypt
from App.models import Post, User


class RegistrationForm(FlaskForm):
	"""
	Our Registration Form Class
	"""
	# Username Field
	username = StringField(
            'Usename', id="username",
            validators=[DataRequired(message="choose your username"),
                        Length(min=4, max=20)],
            description="Your Username")
	# Email Field
	email = StringField(
		'Email Address', id="email",
		validators=[DataRequired(message="please fill in your email address"),
                    Email()],
		description="Your Email Address",)
	# Password Field
	password = PasswordField(
            'Password', id="password",
            validators=[DataRequired(message="your password"),
                        Length(
		min=6, max=16, message='Your password must be a minimum of 6 - 16 charaters'),
                EqualTo('confirm_password', message='Your Passwords must match')])
	# Password Confirmation Field
	confirm_password = PasswordField(
            'Repeat Password', id="confirm_password",
          		validators=[DataRequired(message="confirm password"),
                            EqualTo('password', message='Your Passwords must match')])
	remember = BooleanField('Remember Me', default='checked')
	submit = SubmitField('Sign Up' , id="submit")

	def validate_username(self, username):
		""""our function that ensures that a user username\n
		is unique from that of other users """

		username = User.query.filter_by(username=username.data).first()
		if username:
			raise ValidationError(
				f'Sorry @{username.username} is already taken 😥, Please try a diifrent one ')

	def validate_email(self, email):
		"""our function that ensures that a user email\n
		is unique from that of other users """

		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError(
				f'Sorry that email already exists 😥, Please try a diffrent one ')


class LoginForm(FlaskForm):
	"""
	Our Login Form Class To Login the user
	"""
	# Email Field
	email = StringField(
		'Email',id="email",
		validators=[DataRequired(message="fill in your email address"), Email()],
		description="Your Email Address")
	# Password Field
	password = PasswordField(
            'Password',id="password",
            validators=[DataRequired(message="your password"),
                        Length(min=6, max=16, message='Your password must be a minimum of 6 - 16 charaters')])
	remember = BooleanField('Remember Me', default='checked')
	submit = SubmitField('Log In')

	
	def validate_email(self, email):
		email = User.query.filter_by(email = email.data).first()
		if email:
			pass
		else:
			raise ValidationError(f"Sorry that email doesn't match our records ")

	
	# def validate_password(self, password):
	# 	hw_password = bcrypt.generate_password_hash(password.data).decode('UTF-8')
	# 	password = User.query.filter_by(password = hw_password).first()
	# 	if password:
	# 		pass
	# 	else:
	# 		raise ValidationError(f"Incorrect Password!")
		

class createPost (FlaskForm):
	"""
	Our Blog Post Form Class To let users create posts
	"""
	title = StringField("title", validators=[
	                    DataRequired(message="you must provide a title")])
	content = TextAreaField('Post Content', validators=[DataRequired()])
	submit = SubmitField('Publish')
