"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, login_manager, db
from flask import render_template, request, jsonify, send_file, flash, url_for, redirect
from flask_login import login_user, logout_user, current_user, login_required
import os
from app.forms import LoginForm, RegisterForm
from app.models import Users
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash


###
# Routing for your application.
###

@app.route('/home')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/explore')
def explore():
    """Render website's home page."""
    return render_template('explore.html')

@app.route('/profile')
def profile():
    """Render website's home page."""
    return render_template('profile.html')

@app.route('/logout')
def logout():
    """Render website's home page."""
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


@app.route('/', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = db.session.execute(db.select(Users).filter_by(username=username)).scalar()

        if user is not None and check_password_hash(user.password, password):
            remember_me = False

            if 'remember_me' in request.form:
                remember_me = True
            
            login_user(user, remember=remember_me)
            flash('Logged in Successfully.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Username or Password is incorrect.', 'danger')
    
    return render_template("login.html", form=form)

@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(Users).filter_by(id=id)).scalar()

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        fname = form.fname.data
        lname = form.lname.data
        email = form.email.data
        location = form.location.data
        bio = form.bio.data
        photo = form.photo.data

        filename = secure_filename(photo.filename)
        photo.save(os.path.join('uploads', filename))

        User = Users(username=username, password=password, firstname=fname, 
                     lastname=lname, email=email, location=location, biography=bio, 
                     profile_photo=filename)
        
        if User is not None:
            db.session.add(User)
            db.session.commit()

            flash('User Created')
            return redirect(url_for('home'))

    return render_template("register.html", form=form)


###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404