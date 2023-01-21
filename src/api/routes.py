"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Inventory, Scheduling, Order
from api.utils import generate_sitemap, APIException
from random import randint

api = Blueprint('api', __name__)
    
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

#API user GET by id
@api.route('/users/<int:id>', methods = ['GET'])
def id_users(id):
    users_db = User.query.get(id)
    if users_db is None:
        return "No existe usuario", 404
    return users_db.serialize(), 200
    
#API POST Sing in <---
@api.route('/signin/users', methods = ['POST'])
def add_user():
    request_body = request.json 
    user = User(request_body["name"], request_body["last_name"], request_body["email"], request_body["address"], request_body["password"], request_body["type"])
    db.session.add(user)
    db.session.commit()
    return "Done", 200








"""    

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



#API INVENTORY POST
@api.route('/inventory/users', methods = ['POST'])
def inventory_user():
    inventory1 = Invetory.query.all()
    inventory1 = list(map(lambda inventory1:inventory1.serialize(), inventory_db))
  #  request_body = request.json 
    _inventory.append(request_body)
    return jsonify(_inventory), 200

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