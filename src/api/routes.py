"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Inventory
from api.utils import generate_sitemap, APIException
from random import randint
import uuid
from  werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required


api = Blueprint('api', __name__)
    
#def generate_id():
 #   return randint(0, 99999999)

#welcome to our job
@api.route('/')
def root():
    return jsonify("Bienvenidos a nuestro trabajo")


@api.route('/signin', methods = ['POST'])
def signin():
    
    info = request.form('name', 'last_name', 'email', 'addres', 'password')

    user = User.query\
        .filter_by(email = email)\
        .first()

    if not user:
        user = User(
            id = str((uuid.uuid4())), 
            last_name= last_name,
            email = email, 
            password = generate_password_hash(password),
            type= type  
            
        )
        db.session.add(user)
        de.session.commit()

        return make_response('Successfully registred.', 201)
    else:
        return make_response('User already exist. Please Log in', 202)






#API POST Sing in <---
@api.route('/signin/users', methods = ['POST'])
def add_user():
    request_body = request.json 
    user = User(request_body["name"], request_body["last_name"], request_body["email"], request_body["address"], request_body["password"])
    db.session.add(user)
    db.session.commit()
    return "Done", 200

"""
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
@api.route('/inventory/users', methods = ['POST'])
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
    inventory = Inventory ( request_body["category"], request_body["product"], request_body["picture"], request_body["description"], request_body["price"], request_body["user_id"])    
    return "Done", 200





  

   #API GET user by id
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





#API inventory GET testing <----
@api.route('/inventory', methods = ['GET'])
def all_inventory():
    inventory_db = Inventory.query.all()
    inventory_db = list(map(lambda inventory_db:inventory_db.serialize(), inventory_db))

    return jsonify(inventory_db), 200

#API scheduling GET testing <----
@api.route('/scheduling', methods = ['GET'])
def all_scheduling():
    scheduling_db = Scheduling.query.all()
    scheduling_db = list(map(lambda scheduling_db: scheduling_db.serialize(), scheduling_db))

    return jsonify(scheduling_db), 200

#API order GET testing <----
@api.route('/order', methods = ['GET'])
def all_order():
    order_db = Order.query.all()
    order_db = list(map(lambda order_db: order_db.serialize(), order_db))

    return jsonify(order_db), 200    
    """