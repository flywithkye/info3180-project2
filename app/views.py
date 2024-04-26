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

@app.route('/api/v1/register', methods=['POST'])
def register():
    data = request.get_json()

    if data:
        username = data.get('username')
        password = data.get('password')
        fname = data.get('fname')
        lname = data.get('lname')
        email = data.get('email')
        location = data.get('location')
        bio = data.get('bio')
        photo = data.get('photo')

        # Additional validation can be added here if necessary

        if username and password and fname and lname and email:
            # Save photo to uploads folder
            filename = secure_filename(photo['filename'])
            photo.save(os.path.join('uploads', filename))

            # Create user object
            user = Users(username=username, password=password, firstname=fname, 
                         lastname=lname, email=email, location=location, biography=bio, 
                         profile_photo=filename)

            # Add user to database
            db.session.add(user)
            db.session.commit()

            return jsonify({"message": "User created successfully"}), 201
        else:
            return jsonify({"message": "Missing required fields"}), 400
    else:
        return jsonify({"message": "No data received"}), 400


# @app.route('/api/v1/register' , methods=['POST'])
# def register():
#     data = request.json  # Access JSON data
        
#     # Create a new user instance
#     new_user = User(
#         username=data['username'],
#         password=generate_password_hash(data['password']),
#         firstname=data['firstname'],
#         lastname=data['lastname'],
#         email=data['email'],
#         location = data['location'],
#         biography = data['biography'],
#         phone_number=data.get('phone_number'), 
#     )

#     #I just added this so I can see what is being commited to the db in the console/terminal
#     print(new_user)
    
#     # Add the new user to the database
#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({'message': 'User created successfully'}), 201




# @app.route('/api/v1/auth/login' , methods=['POST'])
# def login():
#     form = LoginForm()

#     if form.validate_on_submit():
#         # Get the username and password values from the form.
#         username = form.username.data
#         password = form.password.data

#         # Using the model, query database for a user based on the username
#         # and password submitted. Then compare the password hash.
#         user = User.query.filter_by(username=username).first()

#         if user and check_password_hash(user.password , password):
            
#             # Login the user
#             login_user(user)

#             # # Remember to flash a message to the user
#             # flash('Login successful!', 'success')

#             # return redirect(url_for('upload'))  # Redirect to the home page
#         # else:
#             # Invalid username or password
#             # flash('Invalid username or password', 'error')

#     return render_template('login.html', form=form)





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