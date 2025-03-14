#!/usr/bin/python3
"""app.py"""
from models import storage
from api.v1.views import app_views
from flask import Flask
from os import getenv
from flask import jsonify
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/api/*": {"origins": "http://0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(error):
    '''The Flask app/request context end event listener.'''
    storage.close()


@app.errorhandler(404)
def page_404(error):
    """ Return a custom 404 error """
    err_dict = {"error": "Not found"}
    return jsonify(err_dict), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
