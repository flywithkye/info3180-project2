# Add any model classes for Flask-SQLAlchemy here
from . import db
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask import url_for

class Posts(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(128))
    photo = db.Column(db.String(80))
    user_id = db.Column(db.Integer, unique=True)
    created_on = db.Column(db.DateTime)

    def __init__(self, id, caption, photo, user_id, created_on):
        self.id = id
        self.caption = caption
        self.photo = photo
        self.user_id = user_id
        self.created_on = created_on

    def serialize(self):
        return {
            "id": self.id,
            "caption": self.caption,
            "photo": self.photo, 
            "user_id": self.user_id,
            "created_on": self.created_on
        }
    
    def _repr_(self):
        return "<User %r>" % self.photo

class Likes(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, unique=True)
    user_id = db.Column(db.Integer, unique=True)

    def __init__(self, id, post_id, user_id):
        self.id = id
        self.post_id = post_id
        self.user_id = user_id

    def serialize(self):
        return {
            "id": self.id,
            "post_id": self.post_id,
            "user_id": self.user_id,
        }
    
    def _repr_(self):
        return "<User %r>" % self.post_id

class Follows(db.Model):
    __tablename__ = 'follows'

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, unique=True)
    user_id = db.Column(db.Integer, unique=True)

    def __init__(self, id, follower_id, user_id):
        self.id = id
        self.follower_id = follower_id
        self.user_id = user_id

    def serialize(self):
        return {
            "id": self.id,
            "follower_id": self.follower_id,
            "user_id": self.user_id,
        }
    
    def _repr_(self):
        return "<User %r>" % self.follower_id

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(200))
    firstname = db.Column(db.String(40))
    lastname = db.Column(db.String(40))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(128))
    profile_photo = db.Column(db.String(200))
    joined_on = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, username, password, firstname, lastname, 
                 email, location, biography, profile_photo):
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_photo = profile_photo

    def serialize(self):
        return {
            "username": self.username,
            "password": self.password, 
            "firstname": self.firstname,
            "lastname": self.lastname, 
            "email": self.email,
            "location": self.location,
            "biography": self.biography, 
            "profile_photo": self.profile_photo
        }
    
    def _repr_(self):
        return "<User %r>" % self.caption
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
