import os
import sys  # Import sys module for printing to stderr

from flask import Flask
from flask_restx import Api, Resource

# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
#print(f"APP_SETTINGS value: {app_settings}", file=sys.stderr)
app.config.from_object(app_settings)

# Debugging: Print app.config to stderr
#print(app.config, file=sys.stderr)

# Ping endpoint
class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

api.add_resource(Ping, '/ping')
