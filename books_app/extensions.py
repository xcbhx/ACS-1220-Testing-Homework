from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from books_app.config import Config
import os

app = Flask(__name__)
app.app_context().push()
app.config.from_object(Config)

db = SQLAlchemy(app)

###########################
# Authentication
###########################

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

bcrypt = Bcrypt(app)

from books_app.auth.routes import auth
from books_app.main.routes import main

app.register_blueprint(auth)
app.register_blueprint(main)