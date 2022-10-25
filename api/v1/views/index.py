#!/usr/bin/python3
"""
    general routes
    routes:
        /status:    display "status":"OK"
        /stats:     dispaly total for all classes
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def status():
    """ return JSON of OK status """
    status = {"status": "OK"}
    return jsonify(status)


@app_views.route("/stats")
def count():
    """ return counts of all classes in storage """
    obj_counts = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(obj_counts)
