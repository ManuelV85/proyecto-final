"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from random import randint

api = Blueprint('api', __name__)

_users = [{

            "name/WS_name": "Gokubike",
            "last_name": "",
            "e-mail": "vegita@vegetables.com",
            "password": "gar4gasd2",
            "addres": "somewhere",
            "id": 1010
        },
        {
            "name/WS_name": "Vegetta",
            "last_name": "Sayajin",
            "e-mail": "vegita@vegetables.com",
            "password": "ffaaffaa",
            "addres": "somewhere",
            "id": 2020
        }]

_inventory = [{
                "categoria": "cadenas",
                "marca": "algo"

            },
            {
                "cuerpo": "manubrio",
                "marca": "algossss"
            }
]
    
#def generate_id():
 #   return randint(0, 99999999)

#welcome to our job
@api.route('/')
def root():
    return jsonify("Bienvenidos a nuestro trabajo")

#API user GET
@api.route('/users', methods = ['GET'])
def all_users():
    users_db = User.query.all()
    users_db = list(map(lambda user:user.serialize(), users_db))

    return jsonify(users_db), 200

#API GET user 
@api.route('/login/user/<int:id>', methods = ['GET'])
def login_user(id):
    for  user in (_users):
        if user["id"] == id:
            return jsonify(user), 200
        
    return "USUARIO NO EXISTE", 400

   
#API GET forgot password
@api.route('/password/user/<int:id>', methods = ['GET'])
def password_user(id):
    for  user in (_users):
        if user["id"] == id:
            return jsonify(user), 200
    return "USUARIO NO EXISTE", 400

#API POST Sing in <---
@api.route('/singin/users', methods = ['POST'])
def add_user():
    user = User.query.all()
    user = list(map(lambda p:p.serialize(), User))
    request_body = request.json 
    _users.append(request_body)
    return jsonify(_users), 200

#API INVENTORY POST
@api.route('/inventory/users', methods = ['POST'])
def inventory_user():
    request_body = request.json 
    _inventory.append(request_body)
    return jsonify(_inventory), 200