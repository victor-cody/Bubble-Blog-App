from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime
from post import blog_posts

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c5e5ad2f9f5c107286bf5b1157a7b122f723f6677d34c1f7689ea3063f5d78f0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# initiating Database
db = SQLAlchemy(app)

class User(db.Model):
    ''''Database Table to store user data'''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique = True, nullable= False)
    email = db.Column(db.String(100), unique = True, nullable= False)
    image_file = db.Column(db.String(20), nullable= False, default = 'default.png')
    password = db.Column(db.String(60), nullable= False)
    posts = db.relationship('Post',backref= 'author',lazy = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    ''''Database Table to store user data'''
    id = db.Column(db.Integer, primary_key=True)
    # author = db.Column(db.String(20), unique = True, nullable= False) 
    title = db.Column(db.String(80), nullable= False)
    content = db.Column(db.Text, nullable = False)
    date_posted = db.Column(db.DateTime, nullable= False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"

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


if __name__ == "__main__":
    app.run(debug=True, port=5000)
