#!/usr/bin/python3
"""view for City objects that handles all default RESTFul API actions"""

from flask import jsonify, request, abort
from models import storage
from models.city import City
from api.v1.views import app_views


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_all_cities(state_id):
    """ returns list of all City objects linked to a given State """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    allcities = []
    cities = storage.all("City").values()
    for city in cities:
        if city.state_id == state_id:
            allcities.append(city.to_json())
    return jsonify(allcities)


@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """ handles GET method """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    city = city.to_json()
    return jsonify(city)


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def del_city(city_id):
    """ handles DELETE method """
    empty_dict = {}
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify(empty_dict), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def add_city(state_id):
    """ handles POST method """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, "Not a JSON")
    if 'name' not in data:
        abort(400, "Missing name")
    city = City(**data)
    city.state_id = state_id
    city.save()
    city = city.to_json()
    return jsonify(city), 201


@app_views.route('/cities/<city_id>', methods=['PUT'])
def edit_city(city_id):
    """ handles PUT method """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, "Not a JSON")

    city.name = data['name']
    city.save()
    return jsonify(city.to_dict()), 200
