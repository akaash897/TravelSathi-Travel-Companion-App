# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from models import User

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RideForm(FlaskForm):
    start_location = StringField('Start Location', validators=[DataRequired()])
    end_location = StringField('End Location', validators=[DataRequired()])
    meetup_point = StringField('Meetup Point', validators=[DataRequired()])
    departure_time = StringField('Departure Time', validators=[DataRequired()])
    available_seats = IntegerField('Available Seats', validators=[DataRequired()])
    cost_per_head = FloatField('Cost per Head', validators=[DataRequired()])
    gender_preference = SelectField('Gender Preference', choices=[('male', 'Male Only'), ('female', 'Female Only'), ('co-ed', 'Co-ed')])
    submit = SubmitField('Post Ride')

    def validate_available_seats(self, available_seats):
        if available_seats.data <= 1:
            raise ValidationError('Available seats must be greater than 1.')
