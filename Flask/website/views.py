# will store main views or url end points or actual functioning front end aspect of website.
# will store standard routes for our websites, where user can actually go to.
# Home page / or any place where user can navigate to.
# render_template is a function.

from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Notes
from . import db

# we will define that this file is blueprint of our application, which simply means it has a bunch of roots(URLs) inside it.

views = Blueprint('views', __name__) #we have setup blueprint for our flask app.

@views.route('/', methods=['GET', 'POST']) #whenever this route (/) is hit, home function will be called.
@login_required #home will not be accessible if user has not been logged in.
def home():
    # return "<h1> Test </h1>"
    # as now we have template ready so
    
    if request.method == 'POST':
        # get the notes
        note = request.form.get('note')

        if len(note) < 1 :
            flash("Note is too short!", category="error")
        else:
            # add the note
            new_note = Notes(data=note, user_id=current_user.id)
            # adding notes to db
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category="success")
    return render_template("home.html", user= current_user) #will pass current user to home page. basically in our template we will be able to reference this current user and check if its authenticated 

# now we have defined our blueprints. We now need to register these blueprints inside our .init file.


