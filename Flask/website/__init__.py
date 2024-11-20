# This will make website folder as a Python package. 
# We can import this folder. whatever is in __init__.py file will run automatically, once we import this folder. 

from flask import Flask

def create_app():
    app = Flask(__name__) #initialling our app, __name__: represents name of the file / name of the file which ran
    app.config['SECRET_KEY'] = 'dcsjndsnd cdnsin' #to encrypt our application, think of it like a password. It will encrypt/secure cookies and session data related to our website. In production, never ever share this secret key

    #here we will register those blueprints. (import)

    # importing.
    from .views import views 
    from .auth import auth
    # registeration with flask
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

