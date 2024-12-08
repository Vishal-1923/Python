# This will make website folder as a Python package. 
# We can import this folder. whatever is in __init__.py file will run automatically, once we import this folder. 

from flask import Flask
from os import path
#for sql-alchemy setup
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager #help manage all of log-ing related things.

#defining a new database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) #initialling our app, __name__: represents name of the file / name of the file which ran
    app.config['SECRET_KEY'] = 'dcsjndsnd cdnsin' #to encrypt our application, think of it like a password. It will encrypt/secure cookies and session data related to our website. In production, never ever share this secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'#my sqlite or sql-alchemy database is stored at this location. Basically it will store in Website folder.

    #initialize database by giving it our flask app
    db.init_app(app) #this database is going to be used for this app.

    #here we will register those blueprints. (import)

    # importing.
    from .views import views 
    from .auth import auth
    # registeration with flask
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #we r importing this becoz we need to make sure we load this(models.py) file and it runs and define all those models, before we create or initialize our db.
    from .models import User, Notes

    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #where do we go if we r not logged in?So should flask redirect us if user is not logged in and there's a log in required.
    login_manager.init_app(app) #telling login manager which app we r using
    
    #function
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #telling flask, how we load a user. User.query.get -> very similar to User.query.filter_by except by default it will look for primary key and check if its equal to what we pass. 

    return app

#create db
def create_database(app):
    #will check if db exists and if it not then it creates it.
    if not path.exists('website/' + DB_NAME):
        with app.app_context():  # Bind the app context
            db.create_all()  # No need to pass 'app' here
        print('Created DB!')