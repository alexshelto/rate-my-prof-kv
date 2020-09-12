
import os
from flask import Flask, request, Blueprint, jsonify
from flask_cors import cross_origin

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
    db.remove(User.name == key) #fix this so you just update the value
    db.insert({'name': key, 'score': value})

    return jsonify(status=200)
  
  # key does not already have a value set
  else:
    db.insert({'name': key,'score': value})
    return jsonify(status=200)


@api.route("/api/<string:key>", methods=['GET','DELETE'])
@cross_origin()
def handle_key(key):
  User = Query()
  if(request.method == 'GET'):

    if(db.search(User.name==key)):
      response = jsonify(data=db.search(User.name==key), status=200)
      # response.headers.add('Access-Control-Allow-Origin', '*')
      return response
    
    else:
      response = jsonify(data=db.search(User.name==key), status=202)
      # response.headers.add('Access-Control-Allow-Origin', '*')
      return response

  #Method == DELETE
  else:
    db.remove(User.name == key)
    print("Pair deleted")
    response = jsonify(status=200)
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response


    

  



