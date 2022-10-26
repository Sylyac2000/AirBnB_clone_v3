#!/usr/bin/python3
""" registering blueprint and starting flask """

from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import environ


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, origins="0.0.0.0")


@app.teardown_appcontext
def tear_down(self):
    """ close query after each session """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ a handler for 404 errors that returns a JSON-formatted 404 """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
