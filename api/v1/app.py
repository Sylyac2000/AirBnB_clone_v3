#!/usr/bin/python3
"""
starts a Flask web application
"""

from models import storage
from api.v1.views import app_views
from flask import Flask,  jsonify, render_template, make_response
from flask_cors import CORS
from os import environ
from flask_swagger import swagger

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()

#Swagger(app)

if __name__ == '__main__':
    """ Main  """
    app.run(host='0.0.0.0', port='5000')
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
