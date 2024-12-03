We are going to make a functional website using Python and Flask(Python's Framework).

Topics:
1. Sign up an user
2. Create new user's account
3. How u store them in a database.
4. Log into user accounts.
5. Log out of them.
6. Associating info with specific user.

Crux:
We are devloping a very simple yet full of learning, Notes application.

Project Walkaround:
1. Create an account
2. Add notes/make new notes.
3. Delete notes.
4. Sign out
5. Sign in any pc to your account, u have yr notes.


Notes:

    Flask:
        Flask is a super light-weight framework.
        It allows us to make website really quickly and easily.
        Not as powerfull as django neither used as much in production.
        It is way more simple than django.
        We can create website way faster.

        Installation:
            pip3 install flask <- to install flask 
            pip3 install flask-login <- to use login module of flask
            pip3 install flask-sqlalchemy <- to use databases (ORM for SQL and PostGre SQL, think it of as a "wrapper")

    Creating Flask application:
        ***
        from flask import Flask

        def create_app():
            app = Flask(__name__)
            app.config['SECRET_KEY'] = 'dcsjndsnd cdnsin'
            return app

        ***
        this creates an flask application.

    Runing Flask application:
        ***
        from website import create_app

        app = create_app()

        if __name__ == '__main__':
            app.run(debug=True)
        ***
        this will run my flask app. i.e., we will have a runing webserver.

    JINJA templating Language and HTML templates
        We will put our HTML templates inside templates folder.
        When we render HTML, we call it a Template.
        We call it a template because there's a special templating language that u can use with Flask --------> JINJA.
        This allows us to write a little bit of Python inside of HTML docs.
        So without JS(JavaScript), we can do bunch of work.

        We define a base template, Theme of website.
        Now we will over-ride parts of base template with more specific templates.
            Main content should change as we change the page, rest of the website should remain same.
        
        JS
        -> if u want to write your own JS, u should write or place them in STATIC folder.
        -> so basically in STATIC folder, all the assets are put there. Or simply things which do not change.

        {{ }}: this means we will be writing some kind of Pythonic expression.

        after defining HTML (base.html), we need to use it via using it in some other html files.
        then we need to render views.py and for that we will immport render


        We can also pass variables and values via Jinja to these templates.
        Although there are some limitations but we can do most of the things with it.
        to write an if, we can use {%%} block.

        Sign up Template: actual sign up form 

        We r able to use all these bootstrap class is becoz my base template which we r inheriting from has all these links to bootstrap (CSS and JS)

Right now, if i click on login and signup button, it shows method not allowed.

With websites, we use something called as HTTP -> Hyper Text Transfer Protocol.
There's bunch of method with it,
-> get request\method
-> post request\method : some kind of changes in database /to state of website. When we r doing post request, we r posting with all of info present in my form.
In case of login and signup, we have made method = post thus we r sending a request to the url we r currently on i.e., signup or login that is a post request that has all of info here. So basically it sends all our data to server.
Server needs to interprete that and respond to us or do something based on that post request 
-> put request\method
-> delete 
-> update