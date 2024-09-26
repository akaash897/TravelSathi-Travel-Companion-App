# config.py
import os

class Config:
    SECRET_KEY = 'SKIBIDI'
    # SQLite database path (local file named 'database.db')
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
