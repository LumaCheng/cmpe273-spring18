from flask import Flask
from flask import request, url_for
from flask import json
from werkzeug.contrib.cache import SimpleCache
app = Flask(__name__)

count = 1
user_info = {}

@app.route("/")
def hello():
  return "Hello World!"

@app.route('/users', methods=['POST'])
def post_user():
    global count
    global user_info
    user = {
        'id'  : count,
        'name' : request.form["name"]
    }
    user_info[str(count)] = request.form["name"]
    count = count+1
    response = app.response_class(
        response=json.dumps(user),
        status=201,
        mimetype='application/json'
    )
    return response

@app.route('/users/<userid>', methods=['GET'])
def get_user(userid):
    global user_info
    if userid in user_info:
        user = {
                'id'  : userid,
                'name' : user_info[userid]
        }
        response = app.response_class(
            response=json.dumps(user),
            status=200,
            mimetype='application/json'
        )
        return response
    else:
        return not_found()


@app.route('/users/<userid>', methods=['DELETE'])
def delete_user(userid):
    global user_info
    del user_info[userid]
    response = app.response_class(
        response=json.dumps(userid),
        status=204,
        mimetype='application/json'
    )
    return response

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    response = app.response_class(
        response=json.dumps(message),
        status=404,
        mimetype='application/json'
    )
    return response
