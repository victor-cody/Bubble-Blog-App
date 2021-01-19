from flask import flash, redirect, render_template, request, session, url_for
from flaskblog import app
from flaskblog.forms import LoginForm, RegistrationForm
from flaskblog.post import blog_posts
from flaskblog.models import User , Post
courses = ["The Computer", "My favourite Code", "Best Hacks"]
words = '[" Front-End Engineer", "Content Creator", "YouTube Instructor", "Python Developer", "UI & UI Developer"]'


@app.route("/<name>/")
@app.route("/home/<name>/")
def home(name):
    """ Our home page """
    return render_template('main.html', author_name=name, title=name, user_words=words, ratings=10, course_list=courses)


@app.route("/posts/")
def posts():
    return render_template('posts.html', posts=blog_posts, title="Posts Section")


@app.route("/about/")
def about():
    return "<div> <h1> This is the <u>about<u> Page </h1> </div>"


@app.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = form.username.data
        session["username"] = user
        flash(f'Successfully created Account for {user}!', 'primary')
        return redirect(url_for('posts', posts=blog_posts, title=f"Posts Section - {user}"))
    return render_template('register.html', title='Sign Up Page', form=form)

@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "123456":
            if "username" in session:
                user = session["username"]
                flash(f'Login Successful, Welcome Back {user} ', 'primary')
            else:
                 flash(f'Login Successful, Welcome Back ', 'primary')   
            return redirect(url_for('posts', posts=blog_posts, title="Posts Section"))
        else:
            flash('Login Unsuccessful, Please check that your email and password are correct', 'danger')
    return render_template('login.html', title='Login Page', form=form)
