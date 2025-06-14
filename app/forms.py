from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectMultipleField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import MultipleFileField, FileAllowed
from wtforms.widgets import ListWidget, CheckboxInput

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class SetupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Create Account')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    images = MultipleFileField('Images', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'bmp'], 'Images only!')
    ])
    submit = SubmitField('Create Post')

class SubscribeForm(FlaskForm):
    email = StringField('Your Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Subscribe')