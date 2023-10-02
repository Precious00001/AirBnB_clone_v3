#!/usr/bin/python3
"""Index"""
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from flask import jsonify


@app_views.route('/status')
def get_status():
    '''Gets the status of the API.
    '''
    return jsonify(status='OK')


@app_views.route('/stats')
def stats():
    """
        return dict count of data
    """
    my_dict = {"amenities": storage.count(Amenity),
               "cities": storage.count(City),
               "places": storage.count(Place),
               "reviews": storage.count(Review),
               "states": storage.count(State),
               "users": storage.count(User)}
    return jsonify(my_dict)
