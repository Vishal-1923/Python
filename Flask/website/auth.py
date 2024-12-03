# authentication -> sign in/out

from flask import Blueprint, render_template, request

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
        firstName = request.form.get('firstName')
        password = request.form.get('password')
        password1 = request.form.get('confirmPassword')
        # Checking validity of user, if valid then create a new user if not then not create a user.
        if len(email) < 4:
            pass
        elif len(firstName) < 2:
            pass
        elif password != password1:
            pass
        elif(len(password) < 7):
            pass
        else
            #add user to database 
    
    return render_template("signup.html")