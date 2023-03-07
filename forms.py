from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, URL, Optional

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, validators

class AddPetForm(FlaskForm):
    name = StringField('Name', validators=[validators.DataRequired()])
    species = StringField('Species', validators=[validators.DataRequired(), validators.AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url = StringField('Photo URL', validators=[validators.URL(require_tld=True, message="Invalid URL format")], default="")
    age = IntegerField('Age', validators=[validators.Optional(), validators.NumberRange(min=0, max=30)])
    notes = StringField('Notes')
    available = BooleanField('Available')

class EditPetForm(FlaskForm):
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = StringField('Notes')
    available = BooleanField('Available')
