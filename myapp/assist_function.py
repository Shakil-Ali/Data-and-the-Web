# Imports
from functools import wraps
from flask import Flask, render_template, flash, redirect, url_for, request, session, logging

# EXTRACT 17

# Check if user logged in function
def is_logged_in(f):
	# Pass f to wraps
	@wraps(f)
	# Function wrap
	def wrap(*args, **kwargs):
		# Conditionl if statement to check if logged_in is in session
		if 'logged_in' in session:
			# If so return the f function with following arguments passed
			return f(*args, **kwargs)
			# Conditional else statement
		else:
			# Flash message to inform the user that they are unauthorised and must login
			flash('Unauthorised. Please login', 'danger')
			# return redirect(url_for('login'))
			return redirect('usr/288/'+url_for('login'))
	# Return wrap variable
	return wrap

