



import os
from flask import Flask, request, Blueprint, jsonify
from tinydb import TinyDB, Query, where
from tinydb.operations import delete
from src import db

#creating blueprint
api = Blueprint('api', __name__)


@api.route("/api/<string:key>/<float:value>", methods=['PUT'])
def put_key(key, value):  
  #if the key already exists in the db must update
  User = Query()
  if(db.search(User.name==key)):
    db.update({'name': key, 'score': value})
    return jsonify(status=200)
  
  # key does not already have a value set
  else:
    db.insert({'name': key,'score': value})
    return jsonify(status=200)



@api.route("/api/<string:key>", methods=['GET','DELETE'])
def handle_key(key):
  User = Query()
  if(request.method == 'GET'):

    if(db.search(User.name==key)):
      return jsonify(db.search(User.name==key))
    
    else:
      return jsonify(status=404) #fix to accurate status

  #Method == DELETE
  else:

    db.remove(User.name == key)
    print("Pair deleted")
    return jsonify(status=200)


    

  



