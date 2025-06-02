import logging
from flask_cors import CORS
from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("FLASK_SECRET_KEY", os.urandom(24))
    app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
    CORS(app, supports_credentials=True)

    logging.basicConfig(level=logging.INFO)
    return app



