# Imports
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from flask_mysqldb import MySQL
from flask import session

# EXTRACT 5
# EXTRACT 6
# EXTRACT 16

# Class for register form
class RegisterForm(Form):
	# Create and set name to the string field of 'Name' and use validators to check its length
	name = StringField('Name', [validators.length(min=1, max=50)])
	# Create and set username to the string field of 'Username' and use validators to check its length
	username = StringField('Username', [validators.length(min=4, max=25)])
	# Create and set email to the string field of 'Email' and use validators to check its length
	email = StringField('Email', [validators.length(min=6, max=50)])
	# Create and set password to the password field of 'Password' and use validators to check its length and if the password match
	password = PasswordField('Password', [validators.DataRequired(),validators.EqualTo('confirm', message='Passwords do not match')])
	# Create and set confirm to the password field of 'Confirm Password'
	confirm = PasswordField('Confirm Password')


# Class for Article Form
class ArticleForm(Form):
	# Create and set title to the string field of 'Title' and use validators to check if any data is present
        title = StringField('Title', validators = [validators.DataRequired()])
	# Create and set body to the text area field of 'Body' and use validators to check if any data is present
        body = TextAreaField('Body', validators = [validators.DataRequired()])



