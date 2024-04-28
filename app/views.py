"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, login_manager, db
from flask import render_template, request, jsonify, send_file, flash, url_for, redirect, g, send_from_directory
from functools import wraps
from flask_login import login_user, logout_user, current_user, login_required
import os
import jwt
from datetime import datetime, timedelta
from app.forms import LoginForm, RegisterForm
from app.models import Users
from app.models import Posts

from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from werkzeug.exceptions import BadRequest



# Create a JWT @requires_auth decorator
# This decorator can be used to denote that a specific route should check
# for a valid JWT token before displaying the contents of that route.
def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.headers.get('Authorization', None) # or request.cookies.get('token', None)

    if not auth:
      return jsonify({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'}), 401

    parts = auth.split()

    if parts[0].lower() != 'bearer':
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}), 401
    elif len(parts) == 1:
      return jsonify({'code': 'invalid_header', 'description': 'Token not found'}), 401
    elif len(parts) > 2:
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}), 401

    token = parts[1]
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])

    except jwt.ExpiredSignatureError:
        return jsonify({'code': 'token_expired', 'description': 'token is expired'}), 401
    except jwt.DecodeError:
        return jsonify({'code': 'token_invalid_signature', 'description': 'Token signature is invalid'}), 401

    g.current_user = user = payload
    return f(*args, **kwargs)

  return decorated



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


@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    try:
        username = request.form.get('username')
        print(username)
        password = request.form.get('password')

        if not username or not password:
            raise BadRequest(description='Username or password not provided')

        # Find user by username
        user = Users.query.filter_by(username=username).first()

        # If user not found or password doesn't match, return error
        if not user or not check_password_hash(user.password, password):
            return jsonify({'message': 'Invalid username or password'}), 401

        # Generate JWT token
        access_token = generate_token(user)
        print (access_token)
        
        # return jsonify({"message": "SUCCESS"}), 200
        return jsonify({"access_token": access_token}), 200

    except BadRequest as e:
        return jsonify({'message': str(e)}), 400

    except Exception as e:
        # Handle other exceptions
        return jsonify({'message': 'Internal Server Error'}), 500


@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(Users).filter_by(id=id)).scalar()

@app.route('/api/v1/register', methods=['POST'])
def register():
    # Check if the request contains form data
    if 'photo' not in request.files:
        return jsonify({"message": "No photo uploaded"}), 400

    photo = request.files['photo']
    if photo.filename == '':
        return jsonify({"message": "No selected photo"}), 400

    # Check if the form fields are present
    username = request.form.get('username')
    password = request.form.get('password')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')

    if not all([username, password, fname, lname, email]):
        return jsonify({"message": "Missing required fields"}), 400

    # Save photo to uploads folder
    filename = secure_filename(photo.filename)
    photo.save(os.path.join('uploads', filename))

    # Create user object
    user = Users(username=username, password=password, firstname=fname, 
                 lastname=lname, email=email, location=request.form.get('location'), 
                 biography=request.form.get('bio'), profile_photo=filename)

    # Add user to database
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201



@app.route('/api/v1/users/1/posts', methods=['POST'])
def post():
    # Check if the request contains form data
    if 'photo' not in request.files:
        return jsonify({"message": "No photo uploaded"}), 400

    photo = request.files['photo']
    if photo.filename == '':
        return jsonify({"message": "No selected photo"}), 400

    caption = request.form.get('caption')


    # Save photo to uploads folder
    filename = secure_filename(photo.filename)
    photo.save(os.path.join('uploads', filename))

    # Create post object
    post = Posts(caption=caption, photo=filename , user_id=1g)

    # Add user to database
    db.session.add(post)
    db.session.commit()

    return jsonify({"message": "Photo uploaded successfully"}), 201



@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def getuser(user_id):
    # Fetch all posts for the user with ID user_id
    user = Users.query.filter_by(id=user_id).first()

    # Prepare response data
    # posts_data = []
    # for post in posts:
    userfound = {
            'id': user.id,
            'bio': user.biography,
            'location': user.location,
            'firstname': user.firstname,
            'lastname': user.lastname

        }
        # posts_data.append(post_data)

    # Return posts as JSON response
    return jsonify(userfound), 200







@app.route('/api/v1/users/<int:user_id>/posts', methods=['GET'])
def getpost(user_id):
    # Fetch all posts for the user with ID user_id
    posts = Posts.query.filter_by(user_id=user_id).all()

    # Prepare response data
    posts_data = []
    for post in posts:
        post_data = {
            'id': post.id,
            'caption': post.caption,
            'photo': post.photo,
            'created_on': post.created_on.strftime("%Y-%m-%d %H:%M:%S")
        }
        posts_data.append(post_data)

    # Return posts as JSON response
    return jsonify(posts_data), 200



@app.route('/api/v1/posts', methods=['GET'])
def get_all_posts():
    # Fetch all posts from the database
    all_posts = Posts.query.all()

    # Prepare response data
    posts_data = []
    for post in all_posts:
        post_data = {
            'id': post.id,
            'caption': post.caption,
            'photo': post.photo,
            'user_id': post.user_id,
            'created_on': post.created_on.strftime("%d %b %Y, %H:%M")
        }
        posts_data.append(post_data)

    # Return all posts as JSON response
    return jsonify(data=posts_data), 200


@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


# @app.route("/api/v1/generate-token")
def generate_token(user):
    # Extract user ID from the user object
    user_id = user.id  # Assuming 'id' is the attribute representing the user ID in the User object
    username = user.username  # Assuming 'username' is the attribute representing the username

    timestamp = datetime.utcnow()
    payload = {
        "sub": user_id,
        "username": username,
        "iat": timestamp,
        "exp": timestamp + timedelta(minutes=30)
    }

    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

    return token

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