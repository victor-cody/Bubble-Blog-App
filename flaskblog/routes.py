from flask import flash, redirect, render_template, request, session, url_for
from flask_login import login_user , logout_user, login_required , current_user
from flaskblog import app, bcrypt, db
from flaskblog.forms import LoginForm, RegistrationForm
from flaskblog.models import User, Post
from flaskblog.post import blog_posts

courses = ["The Computer", "My favourite Code", "Best Hacks"]
words = '[" Front-End Engineer", "Content Creator", "YouTube Instructor", "Python Developer", "UI & UI Developer"]'


@app.route("/register/", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('posts'))
	form = RegistrationForm()
	if form.validate_on_submit():
		# hashing user password
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		# creating user account in database
		user = User(username = form.username.data, email = form.email.data, 
					password = hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Successfully created your Account {user.username}!, you can now log in', 'primary')
		return redirect(url_for('login'))
	return render_template('register.html', title='Sign Up Page', form=form)


@app.route("/login/", methods=['GET', 'POST'])
def login():
	# if user is already logged in redirect them back to home page
	if current_user.is_authenticated:
		return redirect(url_for('posts'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email = form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user( user,form.remember.data)
			next_page = request.args.get('next')
			flash(f'Login Successful, Welcome {user.username} ', 'primary')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful, Please check that your email and password are correct', 'danger')
	return render_template('login.html', title='Login Page', form=form)


@app.route("/logout")
@login_required
def logout():
	logout_user()
	flash(f' Logout Successful!', 'primary')
	return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
	user = current_user
	return render_template("user_account.html",user=user, title = f"{user.username} Account Page" )


@app.route("/")
@app.route("/home/")
def home():
	""" Our home page """
	return render_template('main.html', title="Home Page", user_words=words, ratings=10, course_list=courses, users = User.query.all())


@app.route("/posts/")
def posts():
	return render_template('blog_posts.html', posts=blog_posts, title="Posts Section")


@app.route("/post/new/")
@login_required
def new_post():
	return render_template('publish_post.html', title = "New Post")

@app.route("/about/")
def about():
	return "<div> <h1> This is the <u>about<u> Page </h1> </div>"
