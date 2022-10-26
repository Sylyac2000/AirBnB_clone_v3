#!/usr/bin/python3
"""view for Amenity objects that handles all default RESTFul API actions"""

from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_all_amenities():
    """Retrieves all amenity objects in json """
    amenity_list = [am.to_dict() for am in storage.all(Amenity).values()]
    return jsonify(amenity_list)


@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """Retrieves a amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_amenity(amenity_id):
    """ delete amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def add_amenities():
    """create new amenity obj"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    elif "name" not in request.get_json():
        return jsonify({"error": "Missing name"}), 400
    else:
        obj_data = request.get_json()
        obj = Amenity(**obj_data)
        obj.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/amenities/<amenities_id>',
                 methods=['PUT'], strict_slashes=False)
def edit_amenity(amenities_id):
    """update existing amenity object"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    amenity = storage.get(Amenity, amenities_id)
    if amenity is None:
        abort(404)
    amenity_data = request.get_json()
    amenity.name = amenity_data['name']
    amenity.save()
    return jsonify(amenity.to_dict()), 200
