# routes.py
from flask import render_template, redirect, url_for, flash, request
from app import app, db, bcrypt
from models import User, Ride
from forms import RegistrationForm, LoginForm, RideForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    rides = Ride.query.all()
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

# Join a Ride
@app.route('/ride/join/<int:ride_id>')
@login_required
def join_ride(ride_id):
    ride = Ride.query.get_or_404(ride_id)
    if ride.available_seats > 0:
        ride.passengers.append(current_user)  # This should now work correctly
        ride.available_seats -= 1
        db.session.commit()
        flash('You have successfully joined the ride!', 'success')
    else:
        flash('No seats available for this ride.', 'danger')
    return redirect(url_for('home'))


# routes.py
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

