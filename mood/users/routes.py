from mood import db, bcrypt
from mood.models import User
from mood.users.forms import RegisterForm, LoginForm
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, login_required, logout_user
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, date, timedelta


users = Blueprint('users', __name__)

def already_logged_in():
    flash('You are already logged in!')
    return redirect(url_for('main.index'))

def streak_check():
    current_time = datetime.now().strftime('%H:%M:%S')
    users = User.query.all()

    # Once midnight is reached
    if (current_time == '00:00:00'):
        # Update all user streaks
        for user in users:
            # If user did not input a mood yesterday, reset the user's streak
            if user.mood.created_at.strftime('%Y-%m-%d') != (date.today() - timedelta(days=1)):
                user.streak = 0
                db.session.commit()

# Continuously run streak_check in the background every 1 second
sched = BackgroundScheduler(daemon=True)
sched.add_job(streak_check,'interval',seconds=1)
sched.start()

# Signup Page
@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return already_logged_in()
    form = RegisterForm()
    if form.validate_on_submit():
        flash("Registration successful!")
        email = form.email.data
        username = form.username.data
        password = bcrypt.generate_password_hash(form.password.data)
        user = User(email=email, username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('users/register.html', title='Register', form=form)

# Login Page
@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return already_logged_in()
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Logged in as ' + user.username)
            return redirect(url_for('main.index'))
        else:
            flash("Incorrect username or password.")
            return redirect(url_for('users.login'))
    return render_template('users/login.html', title='Login', form=form)

@users.route('/logout')
@login_required
def logout():
    flash("Logged out of " + current_user.username)
    logout_user()
    return redirect(url_for('main.index'))
