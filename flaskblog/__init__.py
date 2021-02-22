from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flaskblog import routes

app = Flask(__name__)
# app configurations
app.config['SECRET_KEY'] = 'c5e5ad2f9f5c107286bf5b1157a7b122f723f6677d34c1f7689ea3063f5d78f0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bubble-blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# initiating Database
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "info"
