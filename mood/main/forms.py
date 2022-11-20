from flask_wtf import FlaskForm
from wtforms import SubmitField


class MoodForm(FlaskForm):
    mood = SubmitField()
