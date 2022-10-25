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
    """ return counts of all classes in storage by type """
    obj_total = {}
    classes = {"Amenity": "amenities",
               "City": "cities",
               "Place": "places",
               "Review": "reviews",
               "State": "states",
               "User": "users"}
    for classe in classes:
        count = storage.count(classe)
        obj_total[classes.get(classe)] = count
    return jsonify(obj_total)
