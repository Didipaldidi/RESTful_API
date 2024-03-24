import os
import sys  # Import sys module for printing to stderr

from flask import Flask
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
#print(f"APP_SETTINGS value: {app_settings}", file=sys.stderr)
app.config.from_object(app_settings)

# Debugging: Print app.config to stderr
#print(app.config, file=sys.stderr)

# instantiate the db
db = SQLAlchemy(app)

# model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    activate = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

# Ping endpoint
class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

api.add_resource(Ping, '/ping')
