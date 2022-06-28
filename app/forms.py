from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UrlForm(FlaskForm):
    url = StringField('Enter URL', validators=[DataRequired()])
    submit = SubmitField('Submit')