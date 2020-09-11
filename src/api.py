



import os
from flask import Flask, request, Blueprint, jsonify
from tinydb import TinyDB, Query
from src import db

#creating blueprint
api = Blueprint('api', __name__)


@api.route("/api/<string:key>/<int:value>", methods=['PUT'])
def put_key(key, value):
  if(request.method != 'PUT'):
    print('Incorrect method for put key')
    exit(1)
  

  db.insert({'name': key,'score': value})
  print(db.all())
  return jsonify(status=200)



@api.route("/api/<string:key>", methods=['GET','DELETE'])
def handle_key(key):
  if(request.method == 'GET'):
    print(key)
    User = Query()

    if(db.search(User.name==key)):
      return jsonify(db.search(User.name==key))
    
    else:
      return jsonify(status=404) #fix to accurate status
    

  



