from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired(),Length(min=8,max=20)])
	password = PasswordField('Password',validators=[DataRequired()])
	submit = SubmitField('Login')
class ContactForm(FlaskForm):
        body = TextAreaField('Message Body',validators=[DataRequired()])
        submit = SubmitField('Send Email')
class FeedForm(FlaskForm):
        body = TextAreaField('Your feedback is our chance of improvement',validators=[DataRequired()])
        submit = SubmitField('Submit Feedback')
class MediForm(FlaskForm):
        query=StringField('query',validators=[DataRequired()])
        submit=SubmitField('Ask query')

class DelForm(FlaskForm):
	file=StringField('file',validators=[DataRequired()])
	submit=SubmitField('Delete File')
