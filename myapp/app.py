# Import statements
# EXTRACT 1
from flask import Flask, render_template, flash, redirect, url_for, request, session, logging
from flask_mysqldb import MySQL
# EXTRACT 17
from flask_login import user_loaded_from_header
# EXTRACT 16
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
# from functools import wraps
from flask_wtf.csrf import CSRFProtect
from flask import jsonify
import datetime
# EXTRACT 21
from flask_sqlalchemy import SQLAlchemy

# EXTRACT 20

# API imports
from flask_restful import Resource, Api
from flask_restful import fields, marshal_with
from flask_restful import reqparse

# Classes are imported from classes.py
from classes import *

# Assistant function imports function to this file
from assist_function import *

# Set app to flask and pass python file name
app = Flask(__name__)

# Set up the API
api = Api(app)

# Instance of CSRF
csrf = CSRFProtect(app)

# Secret key intialisation
app.secret_key = 'A0Zr98j/3yX R~X:HH!jmN]LWX/,?RT'

# Resource fields being set up
resource_fields = {
	'id': fields.Integer,
	'title': fields.String,
	'author': fields.String,
	'body': fields.String,
	'create_date': fields.DateTime(dt_format='rfc822')
}

# Parser and verify api inputs
parser = reqparse.RequestParser()
parser.add_argument('id', type=int, help='id of article; must be an integer')
parser.add_argument('title', type=str, help='name of article; a string')
parser.add_argument('author', type=str, help='name of author; must be string')
parser.add_argument('body', type=str, help='body of text, must be a string')

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Roadman123'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialise MySQL
mysql = MySQL(app)


# EXTRACT 19

# Article Api Class
class ArticleApi(Resource):
	# Decorator which filters output
	@marshal_with(resource_fields)
	# Function 
	def get(self):
		# Create cursor
		cur = mysql.connection.cursor()
		# Get articles
		result = cur.execute("SELECT * FROM articles")
		# Set article to fetchall on the cursor object
		article = cur.fetchall()
		# Close the connection
		cur.close()
		# Return the articles
		return article


# Article ID Api Class
class ArticlesIdApi(Resource):
	# Decorator which filters output
	@marshal_with(resource_fields)
	# Function for get
	def get(self, id):
		# Create cursor
		cur = mysql.connection.cursor()
		# Get articles
		result = cur.execute("SELECT * FROM articles WHERE id=%s", [id])
		# Set result to the cursor object and execute
		article = cur.fetchone()
		# Close the connection
		cur.close()
		# Return the article
		return article

	
	# Decorator which filters output
	@marshal_with(resource_fields)
	# Function for delete
	def delete(self, id):
		# Cursor is created
		cur = mysql.connection.cursor()
		# Execute the command which will delete the articles
		result = cur.execute("DELETE FROM articles WHERE id=%s", [id])
		# Commit to the database
		mysql.connection.commit()
		# Store all the articles in result 
		result = cur.execute("SELECT * FROM articles")
		# Set article variable to all get all the articles
		article = cur.fetchall()
		# Close the connection
		cur.close()
		# Return the articles
		return article	


	# Decorator which filters output
	@marshal_with(resource_fields)
	def put(self, id):
		# Sets args to the parser with parse_args
		args = parser.parse_args()
		# Store the body as the args parser
		main_body = args['body']
		# Create a cursor which which handles queries
		cur = mysql.connection.cursor()
		# Set variable to string to inform about update/edit
		test_edit_api = "UPDATE API"
		# Execute update command to the article
		cur.execute("UPDATE articles SET title=%s, body=%s WHERE id=%s", (test_edit_api, main_body, id))
		# Commit to the database
		mysql.connection.commit()
		# Close the connection
		cur.close()
		# Return statement to finish execution
		return


	# Decorator which filters output
	@marshal_with(resource_fields)
	def post(self, id):
		# Create cursor
		cur = mysql.connection.cursor()
		# Get articles
		result = cur.execute("SELECT * FROM articles")
		# Set fetchall to article
		article = cur.fetchall()
		# Close the connection
		cur.close()
		# Return the article
		return article
	

# API add resource with routes
api.add_resource(ArticleApi, '/restfapi')
api.add_resource(ArticlesIdApi,'/restfapi/<int:id>')



# EXTRACT 2

# Default/home page
@app.route('/')
# Index function
def index():
	# Return home.html 
	return render_template('home.html')


# About
@app.route('/about')
# About function
def about():
	# Return about.html
	return render_template('about.html')

# Articles
@app.route('/articles')
# Articles function
def articles():
        # Create cursor
        cur = mysql.connection.cursor()
        # Get articles
        result = cur.execute("SELECT * FROM articles")
	# Set article to get all articles
        articles = cur.fetchall()
	# Conditional if to check if result is greater than 0
        if result > 0:
		# Return articles.html with articles variable passed onto it
                return render_template('articles.html', articles=articles)
	# Conditional else statement
        else:
		# Create msg variable and initialise to message for user
                msg = 'No Articles Found'
		# Return articles.html with msg passed on to the articles page
                return render_template('articles.html', msg=msg)
        # Close connection
        cur.close()


# Articles in Articles page
@app.route('/article/<string:id>/')
# Article function
def article(id):
	 # Create cursor
        cur = mysql.connection.cursor()
        # Get articles
        result = cur.execute("SELECT * FROM articles WHERE id=%s", [id])
	# Set article to the one that matches
        article = cur.fetchone()
	# Return article.html page with article variable passed onto it
        return render_template('article.html', article=article)


# Stadiums page
@app.route('/stadium', methods = ['GET', 'POST'])
# Stadium function
def stadium():
	# Conditional if statement to check if the request method is a POST request
	if request.method == 'POST':
		# Variable location set to the request form 'location'
		location = request.form['location']
		# Return stadium html with the location user enetered
		return redirect('usr/288/stadium/'+str(location))
	# Return the stadium.html page
	return render_template('stadium.html')


# Stadiums extra page
@app.route('/stadium/<name>', methods = ['GET', 'POST'])
# Stadiums function
def stadiums(name=None):
	# Conditional if statement to check if request method if POST request
	if request.method == 'POST':
		# Set variable location to the request form 'location'
		location = request.form['location']
		# Return the stadium.html with the location user entered
		return redirect('usr/288/stadium/'+str(location))
	# Return stadium.html page
	return render_template('stadium.html', name=name)


# Scores page
@app.route('/scores')
# Score function
def scores():
	# Return scores.html page
	return render_template('scores.html')


# EXTRACT 12

# User register
@app.route('/register', methods=['GET', 'POST'])
# Register function
def register():
	# Set form variable to equal the class RegisterForm with request.form passed to it
	form = RegisterForm(request.form)
	# Conditional if to check if request method is POST request and if form has been validated
	if request.method == 'POST' and form.validate():
		# Set the name variable to the name from the form
		name = form.name.data 
		# Set the email variable to the email from the form
		email = form.email.data
		# Set the username variable to the username from the form
		username = form.username.data
		# Set password variable to the password from the form (but after it has been encrypted by sha256 which by default adds a salt)
		# EXTRACT 18
		password = sha256_crypt.encrypt(str(form.password.data))
		# Create cursor
		cur = mysql.connection.cursor()
		# Variable result set to get all the users which match with the passed username
		result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
		# Conditional if to check if result is greater than 0
		if result > 0:
			# EXTRACT 7
			# Display a flash warning informing the user, username has already been used
			flash('Username Taken', 'danger')
			# Return the user to the register.html page with form variable passed onto it
			return  render_template('register.html', form=form)
		# Else conditional
		else:
			# Execute query
			cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))
			# Commit to DB
			mysql.connection.commit()
			# Close the connection
			cur.close()
			# Display a flash success message to inform user their account has been successfully created
			flash('You are now registered and can log in', 'success')
			# return redirect(url_for('login'))
			return redirect('usr/288/'+url_for('login'))
	# Return the register.html page with form variable passed onto it
	return render_template('register.html', form=form)


# EXTRACT 10 
# EXTRACT 11

# User Login
@app.route('/login', methods=['GET', 'POST'])
# Login function
def login():
	# Conditional if statement to check if request method is POST request
	if request.method == 'POST':
		# Get Form Fields
		username = request.form['username']
		# Get Form Fields
		password_candidate = request.form['password']
		# Create cursor
		cur = mysql.connection.cursor()
		# Get user by username
		result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
		# Conditional if statement to check if result is greater than 0
		if result > 0:
			# Get stored hash
			data = cur.fetchone()
			# Set the password to the password store in data
			password = data['password']
			# Compare the passwords
			if sha256_crypt.verify(password_candidate, password):
				# Passed and session logged_in is true
				session['logged_in'] = True
				# # username is set to username
				session['username'] = username
				# Flash message to inform the user they have successfully logged in
				flash('You are now logged in', 'success')
				# return the dashboard.html page
				return redirect('usr/288/'+url_for('dashboard'))
			# Conditional else statement
			else:
				# Create and set error variable to an error message
				error = "Invalid login"
				# If the failed to login, login.html will be displayed and error variable will be passed onto it
				return render_template('login.html', error=error)
			# Close connection
			cur.close()
		# Conditional else statement
		else:
			# Set error varible to an error message regarding username not being identified
			error = "Username not found"
			# Return the login.html page with error variable passed onto it
			return render_template('login.html', error=error)
	# Return the login.html page
	return render_template('login.html')



# EXTRACT 13

# Logout
@app.route('/logout')
# Decorator @is_logged_in is placed on logout function
@is_logged_in
# Function logout
def logout():
	# Clear the session
	session.clear()
	# Display message to user, informing them they are logged out
	flash('You are now logged out', 'success')
	# return login.html page to user
	return redirect('usr/288/'+url_for('login'))


# Dashboard
@app.route('/dashboard')
# Decorator @is_logged_in is placed on dashboard function
@is_logged_in
# Dashboard function
def dashboard():
	# Create cursor
	cur = mysql.connection.cursor()
	# Show articles only from user logged in
	result = cur.execute("SELECT * FROM articles WHERE author = %s", [session['username']])
	# Set article variable to all of the matching articles found
	articles = cur.fetchall()
	# Conditional if to check if result greater than 0
	if result > 0:
		# If it is, return the dashboard.html page with the articles variables onto it
		return render_template('dashboard.html', articles=articles)
	# Conditional else statement
	else:
		# Create and set message to inform user about no articles being found
		msg = 'No Articles Found'
		# Return the dashboard.html page with error message passed on
		return render_template('dashboard.html', msg=msg)
	# Close connection
	cur.close()	


# EXTRACT 8
# EXTRACT 9

# Add article
@app.route('/add_article', methods=['GET', 'POST'])
# Decorator @is_logged_in is placed on add_article function
@is_logged_in
# Function to add article
def add_article():
	# Set form variable to ArticleForm class with request.form passed to it
	form = ArticleForm(request.form)
	# Conditional if to check if request method is a POST method and has been validated
	if request.method == 'POST' and form.validate():
		# Set title variable to the title from the form data
		title = form.title.data
		# Set the body variable to the body from the body data
		body = form.body.data
		# Create cursor
		cur = mysql.connection.cursor()
		# Execute the SQL command to insert the required fields into the databases
		cur.execute("INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)", (title, body, session['username']))
		# Commit to DB
		mysql.connection.commit()
		# Close connection
		cur.close()
		# Flash message to inform the user that they have successfully created an article
		flash('Article created', 'success')
		# Return the dashboard.html page
		return redirect('usr/288/'+url_for('dashboard'))
	# Return the add_article.html page with form passed onto it
	return render_template('add_article.html', form=form)


# Edit article
@app.route('/edit_article/<string:id>', methods=['GET', 'POST'])
# Decorator @is_logged_in is placed on edit_article function
@is_logged_in
# Function edit_article 
def edit_article(id):
	# Create cursor 
	cur = mysql.connection.cursor()
	# Get the article by its ID
	result = cur.execute("SELECT * FROM articles WHERE id=%s", [id])
	# Set article to the result which has ID matched
	article = cur.fetchone()
	# Set form the ArticleForm class with request.form passed to it
	form = ArticleForm(request.form)
	# Populat Article Form Fields, set the title of the form data to the title passed by the user for that article
	form.title.data = article['title']
	# Set the body of the form data to the body passed by the user for that article
	form.body.data = article['body']
	# Conditional if to check if the author assoicated with that article is not in session (under that username)
	if article['author'] != session['username']:
		# Display flash message informing the user they have no access unless they log in
		flash('Unauthorised Access', 'danger')
		# Return the dashboard.html page
		return redirect('usr/288/'+url_for('dashboard'))
	# Conditional if to check if request.method is a POST method and if it is validated
	if request.method == 'POST' and form.validate():
		# Set the title variable to the title from the request form
		title = request.form['title']
		# Set thr body variable to the body from the request form
		body = request.form['body']
		# Create cursor
		cur = mysql.connection.cursor()
		# Execute update command
		cur.execute("UPDATE articles SET title=%s, body=%s WHERE id=%s", (title, body, id))
		# Commit to database
		mysql.connection.commit()
		# Close connection
		cur.close()
		# Display flasg message which informs user they have successfully updated an article 
		flash('Article Updated', 'success')
		# Return the dashboard.html page
		return redirect('usr/288/'+url_for('dashboard'))
	# Return the edit_article.html page with form variable passed onto it
	return render_template('edit_article.html', form=form)


# Delete Article
@app.route('/delete_article/<string:id>', methods=['POST'])
# Decorator @is_logged_in is placed on delete_article function
@is_logged_in
# Delete_article function
def delete_article(id):
	# Create cursor
	cur = mysql.connection.cursor()
	# Excecute delete command
	cur.execute("DELETE FROM articles WHERE id=%s", [id])
	# Commit to database
	mysql.connection.commit()
	# Close connection
	cur.close()
	# Flash message to inform the user the article has been deleted
	flash('Article Deleted', 'success')
	# Return the dashboard.html page
	return redirect('usr/288/'+url_for('dashboard'))


# EXTRACT 14 
# EXTRACT 15 (CLICK 'API' ON NAVBAR FOR SIMPLE API, PASS A USERNAME AS AN ADDITIONAL ARGUMENT IF YOU WANT TO SEE ARTICLES FROM THAT USER)

# API (Simlple API - route one for all articles in database, route 2 for articles associated with a specific user)
@app.route('/api')
@app.route('/api/<username>')
# Function api
def api(username=None):
	# Condtional if statement to check if username passed, so can use route 2
	if username:
		# Create and set cur to an sql cursor object
		cur = mysql.connection.cursor()
		# Create and set result to the command which finds all the articles created by a specific user
		result = cur.execute("SELECT * FROM articles WHERE author = %s", [username])
		# Set articles to all the articles associated with that user
		articles = cur.fetchall()
		# Close the connection
		cur.close()
		# Return the jsonify of the articles by that user
		return jsonify({'Forum Posts':articles})
	# Conditional else statement
	else:
		# Create a cursor object
		cur = mysql.connection.cursor()
		# Set result variable to the command which selects all the articles
		result = cur.execute("SELECT * FROM articles")
		# Set articles to all of the articles
		articles = cur.fetchall()
		# Close the connection
		cur.close()
		# Return the jsonify of all the articles
		return jsonify({'Article Posts':articles})


# Check if the python file is valid (Also contains the debug=True)
if __name__ == '__main__':
	# app.secret_key='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
	# Secret key for CSRF
	app.WTF_CSRF_SECRET_KEY='shakilsecret'
	# Set debug to true
	app.run(debug=False, host='0.0.0.0', port=8000)



