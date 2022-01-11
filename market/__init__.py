import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/standm/dev/marketplace/market/market.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY']='1f5f44d9fbe3bc914dc0f38c'
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

from market import routes
