# will store main views or url end points or actual functioning front end aspect of website.
# will store standard routes for our websites, where user can actually go to.
# Home page / or any place where user can navigate to.
# render_template is a function.

from flask import Blueprint, render_template
from flask_login import login_required, current_user


# we will define that this file is blueprint of our application, which simply means it has a bunch of roots(URLs) inside it.

views = Blueprint('views', __name__) #we have setup blueprint for our flask app.

@views.route('/') #whenever this route (/) is hit, home function will be called.
@login_required #home will not be accessible if user has not been logged in.
def home():
    # return "<h1> Test </h1>"
    # as now we have template ready so
    return render_template("home.html")

# now we have defined our blueprints. We now need to register these blueprints inside our .init file.


