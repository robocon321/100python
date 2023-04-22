from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField
import email_validator

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    email = StringField(label = "Email", validators=[DataRequired(), Email()])
    password = PasswordField(label = "Password", validators=[DataRequired()])
    name = StringField(label = "Name", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class LoginForm(FlaskForm):
    email = StringField(label = "Email", validators=[DataRequired(), Email()])
    password = PasswordField(label = "Password", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class CommentForm(FlaskForm):
    body = CKEditorField(label = "Comment", validators=[DataRequired()])
    submit = SubmitField("Submit")