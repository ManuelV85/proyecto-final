"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from random import randint
import uuid
from  werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required


api = Blueprint('api', __name__)

"""
@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }
    return jsonify(response_body), 200
"""

@api.route('/signin', methods = ['POST'])
def signin():
    
    name = request.json["name"]
    last_name = request.json["last_name"]
    email = request.json["email"]
    address = request.json["address"]
    password = request.json["password"]

    if not (name and last_name and email):
        return jsonify({"error": "invalid"}), 400

    #checking for a existing user
    user = User.query.filter_by(email = email).first()
    
    if not user:
        user = User(
            id = str(uuid.uuid4()),
            name = name, 
            last_name= last_name,
            email = email, 
            address = address,
            password = generate_password_hash(password),
            is_active = True
                        
        )
        #insert new user
        db.session.add(user)
        de.session.commit()

        return make_response('Successfully registred.', 201)
    else:
        return make_response('User already exist. Please Log in', 202)






#API POST Sing in <--- test for insert data
@api.route('/signin/users', methods = ['POST'])
def add_user():
    request_body = request.json 
    user = User(request_body["name"], request_body["last_name"], request_body["email"], request_body["address"], request_body["password"])
    db.session.add(user)
    db.session.commit()
    return "Done", 200

#API user GET all users
@api.route('/users', methods = ['GET'])
def all_users():
    users_db = User.query.all()
    users_db = list(map(lambda user:user.serialize(), users_db))
    return jsonify(users_db), 200