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

    
#def generate_id():
 #   return randint(0, 99999999)


#API user GET
@api.route('users', methods = ['GET'])
def all_users():

    return jsonify(_users)

#API GET login 
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

#API POST Sing in 
@api.route('/singin/users', methods = ['POST'])
def add_user():
    request_body = request.json 
    _users.append(request_body)
    return "Done", 200