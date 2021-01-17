from flask import Flask, render_template, redirect, url_for, request, flash
from forms import RegistrationForm, LoginForm
from post import blog_posts

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c5e5ad2f9f5c107286bf5b1157a7b122f723f6677d34c1f7689ea3063f5d78f0'
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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = form.username.data
        flash(f'Successfully created Account for {user}!', 'success')
        return redirect(url_for('posts', posts=blog_posts, title=f"Posts Section - {user}"))
    return render_template('register.html', title='Sign Up Page', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "123456":
            flash('Welcome Back !', 'success')
            return redirect(url_for('posts', posts=blog_posts, title="Posts Section"))
        else:
            flash('Login Unsuccessful, Please check that your email and password are correct', 'danger')
    return render_template('login.html', title='Login Page', form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
