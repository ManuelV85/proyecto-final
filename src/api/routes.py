from flask import Flask, request, jsonify, url_for, Blueprint, make_response
from api.models import db, User, Inventory, Ws_store
from api.utils import generate_sitemap, APIException
import uuid
from  werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required
from cloudinary.uploader import upload

api = Blueprint('api', __name__)

#sigin users
@api.route('/signin/users', methods = ['POST'])
def add_user():
    try:
        #objeto json
        
        data = request.json
        print(data)

        #gets email and password
        email = data["email"]
        #checking for existing user
        user = User.query.filter_by(email = email).first()
   
    
        if user is None:
            
            request_body = request.json 
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
            response = jsonify(response= "Se creo usuario exitosamente", status = 200, code = 0)
            response.headers.add('Access-Control-Allow-Origin', '*') #<--- preguntar 
            return response

        return jsonify(response ="usuario ya existe", status = 200, code = 1)
    except Exception as e:
        print(e)


@api.route('/signin/ws', methods = ['POST'])
def add_ws():
    try:
        #objeto json        
        data = request.json
       
        #gets email and password
        email = data["email"]

        #checking for existing user
        ws_store = Ws_store.query.filter_by(email_ws_store = email).first()
   
    
        if ws_store is None:
            request_body = request.json 
            ws_store = Ws_store(
            name_ws_store = request_body["first_name"],
            email_ws_store = request_body["email"],
            password_ws_store = generate_password_hash(request_body["password"]),
            address_ws_store = request_body["address"],
            hours_ws_store = request_body["hours"],
            scheduling_ws_store = request_body['scheduling'] 
            )
            
        #insert ws_store
            db.session.add(ws_store)
            db.session.commit()
            #return make_response("Done", 200) cambio para conectar con front 
            response = jsonify(response = "Done", status = 200, code = 0)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        return jsonify(response ="usuario ya existe", status = 200, code = 1) #<--- la petición esta bien hecha 
    except Exception as e:
        print(e)




@api.route('/login', methods =['POST'])
def login():
    # creates dictionary of form data
    auth = request.json
    ws = None
    user = None
    if not auth or not auth['email'] or not auth['password']:
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
            )
    user = User.query.filter_by(email = auth['email']).first()
    if user is None:
        ws = Ws_store.query.filter_by(email_ws_store = auth['email']).first(
    )
     

    if user is None and ws is None:
        # returns 401 if user does not exist
        return jsonify({"code":3, "response": "Usuario no existe"})

    if user is not None:

        if check_password_hash(user.password, auth['password']) == True:
            # generates the JWT Token

            access_token = create_access_token(identity=user.id)
            print(access_token)
            return jsonify({ "token": access_token, "id": user.id, "type":"user" })
        # returns 403 if password is wrong
        return jsonify({"code":2 , "response": "Usuario o contraseña incorrectos"})
    
    elif ws is not None: 
        if check_password_hash(ws.password_ws_store, auth['password']) == True:
            # generates the JWT Token
            id = ws.id_ws
            access_token = create_access_token(identity=id)
            print(access_token)
            return jsonify({ "token": access_token, "id": ws.id_ws, "type":"ws" })
        # returns 403 if password is wrong
        return jsonify({"code":2 , "response": "Usuario o contraseña incorrectos"})


#API user GET
@api.route('/users', methods = ['GET'])
@jwt_required()
def all_users():
    users_db = User.query.all()
    users_db = list(map(lambda user:user.serialize(), users_db))
    return jsonify(users_db), 200
    
#API user GET by id
@api.route('/users/<id>', methods = ['GET'])
def id_users(id):
    users_db = User.query.get(id)
    if users_db is None:
        return "No existe usuario", 404
    return users_db.serialize(), 200

#API ws_store GET
@api.route('/ws', methods = ['GET'])
def all_ws():
    ws_db = Ws_store.query.all()
    ws_db = list(map(lambda ws_store: ws_store.serialize(), ws_db))
    return jsonify(ws_db), 200


#API INVENTORY POST
@api.route('/users/inventory', methods = ['POST'])
def inventory_user():
    data = request.form
    image = request.files
    print(data)
    print(request.files)
    user = User.query.get(data.get("user_id"))
    if not user: 
        return "usuario no existe", 404
     
    #with store_context(store):
        
    inventory = Inventory (data.get("category"), data.get("product"), "a", data.get("description"), data.get("price"),data.get("user_id"))
    upload(request.files["picture"], public_id= data.get("product")+ "_" + data.get("category"))
    db.session.add(inventory)
    db.session.commit()
       
    return jsonify(response= "Done" , status = 200, code = 1 )

#API inventory get
@api.route('/inventory', methods = ['GET'])
def all_inventory():
    inventory_db = Inventory.query.all()
    inventory_db = list(map(lambda inventory_db:inventory_db.serialize(), inventory_db))
    return jsonify(inventory_db), 200