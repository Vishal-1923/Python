# will store main views or url end points or actual functioning front end aspect of website.
# will store standard routes for our websites, where user can actually go to.
# Home page / or any place where user can navigate to.

from flask import Blueprint

# we will define that this file is blueprint of our application, which simply means it has a bunch of roots(URLs) inside it.

views = Blueprint('views', __name__) #we have setup blueprint for our flask app.

@views.route('/') #whenever this route (/) is hit, home function will be called.
def home():
    return "<h1> Test </h1>"

# now we have defined our blueprints. We now need to register these blueprints inside our .init file.


