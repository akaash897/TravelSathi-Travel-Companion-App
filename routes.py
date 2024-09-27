# routes.py
from flask import render_template, redirect, url_for, flash, request
from app import app, db, bcrypt
from models import User, Ride
from forms import RegistrationForm, LoginForm, RideForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    if current_user.is_authenticated:
        # Filter rides based on gender preference
        if current_user.gender == 'male':
            rides = Ride.query.filter((Ride.gender_preference == 'male') | (Ride.gender_preference == 'co-ed')).all()
        elif current_user.gender == 'female':
            rides = Ride.query.filter((Ride.gender_preference == 'female') | (Ride.gender_preference == 'co-ed')).all()
    else:
        # If the user is not authenticated, only show co-ed rides (for guests)
        rides = Ride.query.filter_by(gender_preference='co-ed').all()

    return render_template('index.html', rides=rides)

# User Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, password=hashed_password, gender=form.gender.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

# Create a Ride
@app.route('/ride/new', methods=['GET', 'POST'])
@login_required
def new_ride():
    form = RideForm()
    if form.validate_on_submit():
        ride = Ride(start_location=form.start_location.data, end_location=form.end_location.data, 
                    meetup_point=form.meetup_point.data, departure_time=form.departure_time.data, 
                    available_seats=form.available_seats.data, cost_per_head=form.cost_per_head.data,
                    gender_preference=form.gender_preference.data, author=current_user)
        db.session.add(ride)
        db.session.commit()
        flash('Your ride has been posted!', 'success')
        return redirect(url_for('home'))
    return render_template('create_ride.html', form=form)

@app.route('/ride/join/<int:ride_id>')
@login_required
def join_ride(ride_id):
    ride = Ride.query.get_or_404(ride_id)

    # Check if the gender preference of the ride matches the user's gender
    if ride.gender_preference == 'male' and current_user.gender != 'male':
        flash('This ride is male-only. You cannot join.', 'danger')
        return redirect(url_for('home'))
    elif ride.gender_preference == 'female' and current_user.gender != 'female':
        flash('This ride is female-only. You cannot join.', 'danger')
        return redirect(url_for('home'))

    # Check if the user is already a passenger in the ride
    if current_user in ride.passengers:
        flash('You have already joined this ride!', 'warning')
        return redirect(url_for('home'))

    # Check if there are available seats
    if ride.available_seats > 0:
        ride.passengers.append(current_user)  # Add the current user to the passengers
        ride.available_seats -= 1  # Decrease available seats
        db.session.commit()  # Commit the changes to the database
        flash('You have successfully joined the ride!', 'success')
    else:
        flash('No seats available for this ride.', 'danger')

    return redirect(url_for('home'))

@app.route('/joined_rides')
@login_required
def joined_rides():
    # Fetch rides that the user has joined
    joined_rides = current_user.rides_joined
    
    # Debugging: print joined rides to console
    for ride in joined_rides:
        print(f"Joined Ride: {ride.start_location} -> {ride.end_location} at {ride.departure_time}")

    return render_template('joined_rides.html', joined_rides=joined_rides)

# routes.py
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

