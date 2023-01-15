"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from random import randint

api = Blueprint('api', __name__)

class structure:
    def __init__(self, nickname):

        self._user_ws = [{

            "name/WS_name": "Gokubike",
            "last_name": "",
            "e-mail": "vegita@vegetables.com",
            "password": "gar4gasd2",
            "addres": "somewhere",
            "id": self._generate_id()
        },
        {
            "name/WS_name": "Vegetta",
            "last_name": "Sayajin",
            "e-mail": "vegita@vegetables.com",
            "password": "gar4gasd2",
            "addres": "somewhere",
            "id": self._generate_id()
        }]

    

#Random ID
def _generate_id(self):
    return randint(0, 99999999)

#API SING IN  "POST"
@api.route('/users', methods = ["POST"])
def add_user():
    request_body = request.json
    user_ws.append(request_body)
    print("test")
    return jsonify(user_ws)

#API LOGIN "GET"
@api.route('/user/<int:id>', methods = ["GET"])
def login_user(user_id):
    print("test id")

    for user in user_ws:
        if user["ID"] == user_id:
            return jsonify(user), 200
    else:
        return "no esta registrado", 400
        
#API FORGOT PW "GET"abs
@api.route('/user/password/<int:id>', methods = ["GET"])
def login_user(user_id):
    
    for user in user_ws:
        if user["ID"] == user_id:
            return jsonify(user), 200
    else:
        return "no esta registrado", 400

#API INVENTORY  "POST"
@api.route('/users/upload', methods = ["POST"])
def add_item():
    request_body = request.json
    user_ws.append(request_body)
    print("test")
    return jsonify(user_ws)

#API CATEGORY/ITEM "GET"abs
@api.route('/user/category/<int:id>', methods = ["GET"])
def category_user(user_id):
    
    for user in user_ws:
        if user["ID"] == user_id:
            return jsonify(user), 200
    else:
        return "no esta registrado", 400

#API reset password
@api.route('user/reset', methods = ["PUT"])
def reset_user(user_id):
    info = request.json
    for user in user_ws:
        if user["ID"] == user_id:
            user_ws = info
            return jsonify(user)
        else:
            return "no existe el usuario", 400

#API inventory 
@api.route('user/inventory', methods = ["PUT"])
def reset_user(user_id):
    info = request.json
    for user in user_ws:
        if user["ID"] == user_id:
            user_ws = info
            return jsonify(user)
        else:
            return "no existe el usuario", 400