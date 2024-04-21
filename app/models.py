<<<<<<< HEAD
# Add any model classes for Flask-SQLAlchemy here
from . import db
from werkzeug.security import generate_password_hash

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

class Likes(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, unique=True)
    user_id = db.Column(db.Integer, unique=True)

    def __init__(self, id, post_id, user_id):
        self.id = id
        self.post_id = post_id
        self.user_id = user_id

class Follows(db.Model):
    __tablename__ = 'follows'

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, unique=True)
    user_id = db.Column(db.Integer, unique=True)

    def __init__(self, id, follower_id, user_id):
        self.id = id
        self.follower_id = follower_id
        self.user_id = user_id

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    firstname = db.Column(db.String(40))
    lastname = db.Column(db.String(40))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(80))
    profile_photo = db.Column(db.String(80))
    joined_on = db.Column(db.DateTime)

    def __init__(self, id, username, password, firstname, lastname, 
                 email, location, biography, profile_photo, joined_on):
        self.id = id
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_photo = profile_photo
        self.joined_on = joined_on
    
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
=======
# Add any model classes for Flask-SQLAlchemy here

#This is just a test by Tareque to see if I can push to the repo
>>>>>>> 119bb3cbc51b4a8dbaf2d3790189f9717f380daa
