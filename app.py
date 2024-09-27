# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db = SQLAlchemy(app)  # Initialize the database
bcrypt = Bcrypt(app)  # For password hashing
login_manager = LoginManager(app)  # Login manager for user authentication

@login_manager.user_loader
def load_user(user_id):
    from models import User  # Import here to avoid circular import
    return User.query.get(int(user_id))  # Retrieve user from the database

@app.before_request
def create_tables():
    from models import User, Ride  # Import here to avoid circular import
    db.create_all()  # Create tables when the app first runs

from routes import *

if __name__ == "__main__":
    app.run(debug=True)


