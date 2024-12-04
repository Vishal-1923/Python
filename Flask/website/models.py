# to store database models
from . import db #from init.py file, we r importing db -> basically importing from current package which in this case is website folder 

from flask_login import UserMixin #usermixin - custom class which we can inherit that gives our user object some things specific for our flask login. Flask login is just a module that helps us log users in. For that our user object needs to inherit from usermixin.

from sqlalchemy.sql import func #We dont need to specify data field ourself, sqlalchemy - func will take care of it.

#whenever u want to make a new db model, u wanna store a diff type of object, u r going to define its name of object and then inherit from db.model + for User object, we also need to inherit from usermixin.
class User(db.Model, UserMixin):
    #here we will define all the columns that we want to store in this table. Simply a schema/ a layout for some object that can be stored in our db
    id = db.Column(db.Integer, primary_key = True) #id is primary key.
    
    email = db.Column(db.String(150), unique=True) #here 150 is max length of that string. Unique means no user can have same email as another user.
    password = db.column(db.String(150))
    first_name = db.Column(db.String(150))

class Notes(db.Model): #more general db model.
    id = db.Column(db.Integer, primary_key = True)
    data = db.Columnb(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default = func.now()) #whenever user is created that time will be stored.