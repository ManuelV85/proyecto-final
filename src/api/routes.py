"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Inventory
from api.utils import generate_sitemap, APIException
import uuid
from  werkzeug.security import generate_password_hash, check_password_hash

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
def add_user():

    """
    #dictionary of the form data
    data = request.form 
    #gets email and password
    email = data.get('email')
    password = data.get('password')
    #checking for existing user
    user = User.query.filter_by(email = email).first()
    
    if not user:
        user = User(
        id = str(uuid.uuid4()),
        first_name = first_name,
        last_name = last_name, 
        email = email,
        password = data.generate_password_hash(password),
        address = address, 
        is_active = True
        )
"""
    request_body = request.json 
    user = User(request_body["first_name"], request_body["last_name"], request_body["email"], request_body["password"], request_body["address"])
   #insert users
    db.session.add(user)
    db.session.commit()
    return "Done", 200

#API user GET
@api.route('/users', methods = ['GET'])
def all_users():
    users_db = User.query.all()
    users_db = list(map(lambda user:user.serialize(), users_db))
    return jsonify(users_db), 200
    
#API user GET by id
@api.route('/users/<int:id>', methods = ['GET'])
def id_users(id):
    users_db = User.query.get(id)
    if users_db is None:
        return "No existe usuario", 404
    return users_db.serialize(), 200


#API INVENTORY POST
@api.route('/users/inventory', methods = ['POST'])
def inventory_user():
    request_body = request.json

   # print(request_body["user_id"])
   # user = User.query.get(request_body["user_id"])
    #if not user: 
    #    return "usuario no existe", 404
    #image_binary = get(request_body[picture]).content
    #print(image_binary)
    #with store_context(store):
     #   inventory.picture.from_blob(image_binary)
    inventory = Inventory ( request_body["category"], request_body["product"], request_body["description"], request_body["price"], request_body["user_id"])    
    return "Done", 200

#API inventory get
@api.route('/inventory', methods = ['GET'])
def all_inventory():
    inventory_db = Inventory.query.all()
    inventory_db = list(map(lambda inventory_db:inventory_db.serialize(), inventory_db))
    return jsonify(inventory_db), 200