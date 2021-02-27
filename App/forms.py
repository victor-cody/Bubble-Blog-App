from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField, TextAreaField, SelectMultipleField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length, Email
from App.models import User, Post


class RegistrationForm(FlaskForm):
	"""
	Our Registration Form Class
	"""
	# Username Field
	username = StringField(
            'Usename',
            validators=[DataRequired(message="choose your username"),
                        Length(min=4, max=20)],
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
		min=6, max=16, message='Your password must be a minimum of 6 - 16 charaters'),
                EqualTo('confirm_password', message='Your Passwords must match')])
	# Password Confirmation Field
	confirm_password = PasswordField(
            'Repeat Password',
          		validators=[DataRequired(message="confirm password"),
                            EqualTo('password', message='Your Passwords must match')])
	remember = BooleanField('Remember Me', default='checked')
	submit = SubmitField('Sign Up')

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
		'Email',
		validators=[DataRequired(message="fill in your email address"), Email()],
		description="Your Email Address")
	# Password Field
	password = PasswordField(
            'Password',
            validators=[DataRequired(message="your password"),
                        Length(min=6, max=16, message='Your password must be a minimum of 6 - 16 charaters')])
	remember = BooleanField('Remember Me', default='checked')
	submit = SubmitField('Log In')


class createPost (FlaskForm):
	"""
	Our Blog Post Form Class To let users create posts
	"""
	title = StringField("title", validators=[
	                    DataRequired(message="you must provide a title")])
	content = TextAreaField('Post Content', validators=[DataRequired()])
	submit = SubmitField('Publish')
