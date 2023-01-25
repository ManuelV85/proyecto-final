"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint, make_response
from api.models import db, User, Inventory, Ws_store
from api.utils import generate_sitemap, APIException
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

@api.route('/signin/users', methods = ['POST'])
def add_user():
    try:
        #objeto json
        print(request.json)
        data = request.json
        print(data)
        #gets email and password
        email = data["email"]
        #checking for existing user
        user = User.query.filter_by(email = email).first()
   
    
        if user is None:
            
            request_body = request.json 
            #user = User(request_body["first_name"], request_body["last_name"], request_body["email"], request_body["password"], request_body["address"])
            user = User(
            first_name = request_body["first_name"],
            last_name = request_body["last_name"], 
            email = request_body["email"],
            password = generate_password_hash(request_body["password"]),
            address = request_body["address"], 
            )
        #insert users
            db.session.add(user)
            db.session.commit()
            #return make_response("Done", 200) cambio para conectar con front 
            response = jsonify(response= "Done", status = 200, code = 0)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        return jsonify(response ="usuario ya existe", status = 200, code = 1) #<--- la petición esta bien hecha 
    except Exception as e:
        print(e)

@api.route('/login', methods =['POST'])
def login():
    # creates dictionary of form data
    auth = request.json

    if not auth or not auth['email'] or not auth['password']:
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
            )

    user = User.query.filter_by(email = auth['email']).first()

    if user is None:
        # returns 401 if user does not exist
        return make_response(
            'El usuario no existe',
            200, #no es una petición mal hecha 
            {'WWW-Authenticate' : 'Basic realm ="Wrong User or Password !!"'}
        )
    print(user.password)
    if check_password_hash(user.password, auth['password']) == True:
        # generates the JWT Token
        access_token = create_access_token(identity=user.id)
        print(access_token)
        return jsonify({ "token": access_token, "user_id": user.id })
    # returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate' : 'Basic realm ="Wrong User or Password !!"'}
    )

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

#APi ws_store 
@api.route('/signin/ws', methods = ['POST'])
def add_ws():
    request_body = request.json
    ws_store_db = Ws_store(request_body["id_ws"], request_body["name_ws_store"], request_body["email_ws_store"], request_body["password_ws_store"], request_body["address_ws_store"], request_body["scheduling_ws_store"])
    db.session.add(ws_store_db)
    db.session.commit()
    return "Done", 200

#API ws_store GET
@api.route('/ws', methods = ['GET'])
def all_ws():
    ws_db = Ws_store.query.all()
    ws_db = list(map(lambda ws_store: ws_store.serialize(), ws_db))
    return jsonify(ws_db), 200


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