# authentication -> sign in/out

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # return "<p> login </p>"
    data = request.form #whenever we access it inside route, it will have info about the request that was sent to access this route.
    #form: all of data which was sent as a part of form.
    print(data) #ImmutableMultiDict([('email', 'kl@gh.com'), ('password', 'uiiops')]) --> it will print like this 
    # this willl only work if we send data i.e., form
    return render_template("login.html", text="testing", boolean = True)

@auth.route('/logout')
def logout():
    return "<p> logout </p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password = request.form.get('password')
        password1 = request.form.get('confirmPassword')
        # Checking validity of user, if valid then create a new user if not then not create a user.
        if len(email) < 4:
            flash('Email must be greater than 4 characters. ', category='error')
        elif len(first_name) < 2:
            flash('First Name must be greater than 2 characters. ', category='error')
        elif password != password1:
            flash('Passwords dont match. ', category='error')
        elif(len(password) < 3):
            flash('Too short Password. ', category='error')
        else:
            # Check if the email already exists
            existing_user = User.query.filter_by(email=email).first()
            
            if existing_user:
                flash("Email is already in use. Please choose a different one.")
                return redirect(url_for('auth.sign_up'))  # or show an error on the signup form
    
            # create a new user.
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password, method='scrypt'))
            # adding user to db
            db.session.add(new_user)
            db.session.commit() #Hey, we have made some changes to db, update it.
            flash('Account created. ', category='success')
            # re-direct user to home page!
            return redirect(url_for('views.home')) #same as saying url_for('/')

    
    return render_template("signup.html")