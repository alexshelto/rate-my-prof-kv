

import os
from flask import Flask, request
from tinydb import TinyDB, Query
app = Flask(__name__)




@app.route("/api/<string:key>/<int:value>", methods=['PUT'])
def put_key(key, value):
  if(request.method != 'PUT'):
    print('Incorrect method for put key')
    exit(1)
  db.insert({'string': key,'int': value})
  pass

@app.route("/api/<string:key>", methods=['GET','DELETE'])
def handle_key(key):
  if(request.method == 'GET'):
    print(key)
    print("HELLO WORLD NOTICE ME")
    User = Query()
    print(db.search(User.name == 'Chris'))
    # return(db.search(User.name == 'Chris'))
  return("hello")

  



if __name__ == '__main__':
  db = TinyDB('scores.json')
  app.run()