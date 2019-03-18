"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
import werkzeug

from app import app, db#, login_manager
from flask import render_template, request, redirect, url_for, flash
#from flask_login import login_user, logout_user, current_user, login_required
from .forms import Profile, Photo
from werkzeug.security import check_password_hash
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from .models import ProfilesDB
#import UserProfile.user_profiles

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile', methods=['GET', 'POST'])
def new_profile():
    form = Profile()
    if request.method == 'POST':
        if form.validate_on_submit():
            firstname = form.firstname.data
            lastname = form.lastname.data
            email = form.email.data
            location = form. location.data
            gender = form. gender.data
            biography = form.biography.data
            
        
            NewProfile = ProfilesDB(firstname, lastname, email, location, gender,biography) 
            
            db.session.add(NewProfile) 
            db.session.commit()
            
            flash ('PROFILE SUCCESSFULLY CREATED')
            return render_template('profile.html', form=form)
        flash('Please try again; There was an error in creating your Profile')
    return render_template('profile.html', form=Profile)
    
@app.route('/profiles')
def show_profiles():
    form = Profile()
    users = request.form['data']
    users = users.query.all()
    data = {"Profiles": users}
    return render_template('profiles.html', data)

@app.route('/profile/userid')
def ProfileUsers():
    form = Profile()
    email=request.form['email']
    email=Profile.email.query.filter.first()
    if email:
        email=request.form['email']
        return render_template('viewprofile.html', form=form)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
