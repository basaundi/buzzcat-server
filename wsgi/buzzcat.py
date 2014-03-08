#!/usr/bin/env python

from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

@app.route("/")
def index():
    return "Hello World!"

class Profiles(restful.Resource):
    pass

class ChatMessages(restful.Resource):
    def get(self, location_id):
        return {'location_id': location_id, 'hello': 'world'}

    def post(self, location_id, msg):
        pass

api.add_resource(ChatMessages, '/api/chats/<string:location_id>/messages')

if __name__ == "__main__":
    app.run()
