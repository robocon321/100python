from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    cafe_name = StringField(label = 'Cafe Name', validators=[DataRequired()])
    location = StringField(label = 'Cafe Location on Google Maps (URL)', validators=[DataRequired()])
    open = StringField(label = 'Opening time e.g: 8AM', validators=[DataRequired()])
    close = StringField(label = 'Close Time e.g: 5:30PM', validators=[DataRequired()])
    coffee = SelectField(label = 'Coffee Rating', validators=[DataRequired()], validate_choice=[1, 2, 3])
    wifi = StringField(label = 'Wifi Strength Rating', validators=[DataRequired()])
    power = StringField(label = 'Power Socket Availability', validators=[DataRequired()])

