
import os
from flask import Flask
# from flask_cors import CORS 
from tinydb import TinyDB, Query




db = TinyDB('./src/scores.json')#initialize


def create_app():
  app = Flask(__name__)
  # CORS(app)
  # db = TinyDB('./src/scores.json')#initialize
  from src.api import api
  app.register_blueprint(api)

  return app
