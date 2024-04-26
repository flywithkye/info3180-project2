from flask import Flask
from flask_cors import CORS  # Import CORS from flask_cors
from .config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy, Migrate, and LoginManager as before
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Enable CORS for all routes
CORS(app)

from app import views
