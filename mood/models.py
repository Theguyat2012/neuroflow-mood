from mood import db, login_manager
from flask import flash, redirect, url_for
from flask_login import UserMixin
from datetime import datetime


# Enables flask-login to access current_user
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

# Handle flask-login's @login_required decorator
@login_manager.unauthorized_handler
def unauthorized_callback():
    flash('You not logged in!')
    return redirect(url_for('users.login'))

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    email = db.Column(db.String(256), unique=True, nullable=False)
    username = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), unique=True, nullable=False)
    streak = db.Column(db.Integer, default=0, nullable=False)
    mood = db.relationship('Mood', backref='user', lazy=True)

    def __repr__(self) -> str:
        return "<User {}, {}, {}, {}>".format(self.id, self.created_at, self.email, self.username)

# User mood
class Mood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(120), nullable=False)

    def __repr__(self) -> str:
        return "<User {}, {}, {}, {}>".format(self.id, self.created_at, self.user_id, self.status)
