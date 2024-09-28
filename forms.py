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

from wtforms.validators import NumberRange

from wtforms import ValidationError

from wtforms import ValidationError, FloatField, IntegerField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class RideForm(FlaskForm):
    location_choices = [
        ('iit_jodhpur', 'IIT Jodhpur'),
        ('jodhpur_junction', 'Jodhpur Junction'),
        ('airport', 'Jodhpur Airport'),
        ('bus_stand', 'MBM Bus Stand'),
        ('paota', 'Paota')
    ]

    start_location = SelectField('Start Location', choices=location_choices, validators=[DataRequired()])
    end_location = SelectField('End Location', choices=location_choices, validators=[DataRequired()])
    meetup_point = StringField('Meetup Point', validators=[DataRequired()])
    departure_time = StringField('Departure Time', validators=[DataRequired()])
    available_seats = IntegerField('Available Seats', validators=[DataRequired()])
    cost_per_head = FloatField('Cost per Head', validators=[DataRequired()])
    gender_preference = SelectField('Gender Preference', choices=[('male', 'Male Only'), ('female', 'Female Only'), ('co-ed', 'Co-ed')])
    submit = SubmitField('Post Ride')

    # Custom validation for start and end location
    def validate_end_location(self, end_location):
        if self.start_location.data == end_location.data:
            raise ValidationError('End location must be different from start location.')

    # Custom validation for available seats
    def validate_available_seats(self, available_seats):
        if available_seats.data <= 1:
            raise ValidationError('Available seats must be greater than 1.')

    # Custom validation for cost per head
    def validate_cost_per_head(self, cost_per_head):
        if cost_per_head.data is not None and cost_per_head.data <= 0.0:
            raise ValidationError('Cost per head must be greater than 0.')






