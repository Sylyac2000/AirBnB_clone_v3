#!/usr/bin/python3
"""a new view for State objects that handles all default
RESTFul API actions:
"""

from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.state import State


@app_views.route("/states", methods=['GET'], strict_slashes=False)
def get_all_states():
    """Retrieves all State objects"""
    allstates = storage.all(State).values()
    statelist = []
    for state in allstates:
        statelist.append(state.to_dict())
    return jsonify(statelist)


@app_views.route("/states/<state_id>", methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieves a State object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=['DELETE'],
                 strict_slashes=False)
def del_state(state_id):
    """delete a State object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    empty_dict = {}
    return jsonify(empty_dict), 200


@app_views.route("/states", methods=['POST'], strict_slashes=False)
def add_state():
    """Retrieves a State object"""
    data_dict = request.get_json()
    if data_dict is None:
        abort(400, "Not a JSON")
    if 'name' not in data_dict:
        abort(400, "Missing name")
    state = State(**data_dict)
    state.save()
    # state = state.to_json()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def edit_state(state_id):
    """ update a state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, "Not a JSON")

    obj_data = request.get_json()
    state.name = obj_data['name']
    state.save()
    return jsonify(state.to_dict()), 200
