"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Inventory
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

"""
@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200
    """

@api.route('/signin/users', methods = ['POST'])
def add_user():
    request_body = request.json 
    user = User(request_body["first_name"], request_body["last_name"], request_body["email"], request_body["password"], request_body["address"])
    db.session.add(user)
    db.session.commit()
    return "Done", 200

#API user GET
@api.route('/users', methods = ['GET'])
def all_users():
    users_db = User.query.all()
    users_db = list(map(lambda user:user.serialize(), users_db))
    return jsonify(users_db), 200

#API INVENTORY POST
@api.route('/users/inventory', methods = ['POST'])
def inventory_user():
    request_body = request.json
    print(request_body["user_id"])
    user = User.query.get(request_body["user_id"])
    if not user: 
        return "usuario no existe", 404
    image_binary = get(request_body[picture]).content
    print(image_binary)
    #with store_context(store):
     #   inventory.picture.from_blob(image_binary)
    inventory = Inventory ( request_body["category"], request_body["product"], request_body["description"], request_body["price"], request_body["user_id"])    
    return "Done", 200