from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c5e5ad2f9f5c107286bf5b1157a7b122f723f6677d34c1f7689ea3063f5d78f0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# initiating Database
db = SQLAlchemy(app)

from flaskblog import routes