from flask import Flask, request
from json import dumps, loads
from db import find_object, update_object

app = Flask(__name__)

@app.route('/<oid>', methods=['GET'])
def findObject(oid):
  #DB lookup code goes here
  my_object = find_object(oid)
  if my_object is None:
      return "",404
  return dumps(my_object)

@app.route('/<oid>', methods=['POST', 'PUT'])
def updateObject(oid):
  #DB Update/Upsert code goes here
  print(str(request.get_data()))
  update_rqst = loads( str(request.get_data(), 'utf-8'))
  update_rqst['b'] = oid
  update_object(update_rqst)
  print ('I got a post request!')
  return ""

if __name__ == '__main__':
  #with app.test_client() as c:
   # get_resp = c.get('/blah')
   # print ('get status: %s' % get_resp.status)
   # print ('get response: %s' % get_resp.get_data())
   # post_resp = c.post('/blah')
    app.testing = True
    with app.test_client() as c:
        post_resp = c.post('/its_me', data=dumps({"my_name": "Lakhan"}))
        get_resp = c.get('/its_me')
        print ('get status: %s' % get_resp.status)
        print ('get response: %s' % get_resp.get_data())
