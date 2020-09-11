
import os
from flask import Flask
from tinydb import TinyDB, Query




db = TinyDB('./src/scores.json')#initialize


def create_app():
  app = Flask(__name__)
  # db = TinyDB('./src/scores.json')#initialize
  from src.api import api
  app.register_blueprint(api)

  return app
