from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)
# app.static_url_path('templates')
auth = False

courses = ["The Computer", "My favourite Code", "Best Hacks"]

@app.route('/<name>')
@app.route('/home/<name>')
def home(name):
    """Our home page that uses templating"""
    return render_template("index.html", author_name=name, ratings=10, course_list=courses)


# @app.route("/login", methods=['POST', 'GET'])
# def administer():
#     return render_template('login.html', title="Login")


@app.route('/<user>')
def user(user):
    return render_template()


@app.route("/<name>")
def greet(name):
    """principle of using url parameters to create 
    dynamic content in our page"""
    return f"<h1>Hello dear {name}, how are you? </h1>"


@app.route("/redirect")
def redirect():
    return """ 
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Home Page</title> 
    <style>
    div{
        margin:2rem auto;
      width: 60vw;
      height: 50vh;
      display: flex;
      justify-content: space-around;
      align-items: center;
      flex-flow: column nowrap;
      padding: 4rem 0 3rem;
      text-align: center;
      color: darkred;
      font-size: 1.5rem;
    }
    </style>
    </head>
    <body>
      <div>
     <h2>Sorry you can't log in</h2>
    </div> 
    </body>
    </html>
    """


@app.route("/admin/<int:ID>")
def admin(ID):
    if ID == 123:
        return redirect(url_for('greet', name="Admin"))
    else:
        return redirect(url_for("redirect"))


if __name__ == "__main__":
    app.run(debug=True, port=3000)
