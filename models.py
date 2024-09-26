# models.py
from app import db
from flask_login import UserMixin

# Association table for the many-to-many relationship between Users and Rides
ride_passengers = db.Table('ride_passengers',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('ride_id', db.Integer, db.ForeignKey('ride.id'), primary_key=True)
)

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    gender = db.Column(db.String(10), nullable=False)  # 'male', 'female'
    ride_posts = db.relationship('Ride', backref='author', lazy=True)
    rides_joined = db.relationship('Ride', secondary=ride_passengers, backref='passengers')

# Ride model
class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_location = db.Column(db.String(255), nullable=False)
    end_location = db.Column(db.String(255), nullable=False)
    meetup_point = db.Column(db.String(255), nullable=False)
    departure_time = db.Column(db.String(20), nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)
    cost_per_head = db.Column(db.Float, nullable=False)
    gender_preference = db.Column(db.String(10), nullable=False)  # 'male', 'female', 'co-ed'
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Ensure 'user.id' matches the User model
