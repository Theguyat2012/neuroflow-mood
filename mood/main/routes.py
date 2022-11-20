from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from mood import db
from mood.models import Mood
from mood.main.forms import MoodForm
from datetime import datetime
import sys


main = Blueprint('main', __name__)

# Homepage
@main.route('/', methods=['GET'])
def index():
    return render_template('main/index.html', title='Home')

# Access mood form and user's mood statistics and history
@main.route('/mood', methods=['GET', 'POST'])
@login_required
def mood():
    form = MoodForm()
    if form.validate_on_submit():
        # Create mood object
        mood = Mood(user_id=current_user.id, status=request.form['mood'])
        mood_length = len(current_user.mood)
        db.session.add(mood)
        if mood_length == 0:
            current_user.streak += 1
            db.session.commit()
        else:
            # If mood already exists for today, simply replace the mood with a new object, do not add to streak
            if current_user.mood[mood_length-1].created_at.strftime('%Y-%m-%d') == datetime.now().strftime('%Y-%m-%d'):
                db.session.commit()
            else:
                current_user.streak += 1
                db.session.commit()
        flash('Submitted mood: {} '.format(request.form['mood']))
        return redirect(url_for('main.mood'))
    return render_template('main/mood.html', title='Mood', form=form, datetime = datetime)
