from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[validators.Length(min=6, max=120), validators.Email(message=('That\'s not a valid email address.')), DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired(), validators.Length(min=8)])
    submit = SubmitField(label='OK')
