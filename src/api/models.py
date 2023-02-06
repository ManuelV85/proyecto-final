from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    

    def serialize (self):
        return{
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "address": self.address,
           
        }
    
    def __init__(self, first_name, last_name, email, password, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.address = address

    def __repr__(self):
        return f"{self.first_name}: {self.last_name}: {self.email}: {self.password}: {self.address}"


class Ws_store(db.Model):
    __tablename__= 'ws_store'
    id_ws = db.Column(db.Integer, primary_key = True)
    name_ws_store = db.Column(db.String(250), nullable = False)
    email_ws_store = db.Column(db.String(250), nullable = False)
    password_ws_store = db.Column(db.String(250), nullable = False)
    address_ws_store = db.Column(db.String(250), nullable = False)
    hours_ws_store = db.Column(db.String(250), nullable = True)
    scheduling_ws_store = db.Column(db.String(250), nullable = False)

    def serialize (self):
        return {
            "id_ws": self.id_ws,
            "name_ws_store" : self.name_ws_store,
            "email_ws_store": self.email_ws_store,
            "address_ws_store": self.address_ws_store,
            "hours_ws_store": self.hours_ws_store,
            "scheduling_ws_store": self.scheduling_ws_store
        }
    def __init__(self, name_ws_store, email_ws_store, password_ws_store, address_ws_store, hours_ws_store, scheduling_ws_store):
        self.name_ws_store = name_ws_store
        self.email_ws_store = email_ws_store
        self.password_ws_store = password_ws_store
        self.address_ws_store = address_ws_store
        self.hours_ws_store = hours_ws_store
        self.scheduling_ws_store = scheduling_ws_store

    def __repr__(self):
        return f"{self.name_ws_store}: {self.email_ws_store}: {self.passwor_ws_store}: {self.address_ws_store}:{self.hours_ws_store}: {self.scheduling_ws_store}"





class Inventory(db.Model):
    __tablename__ = 'inventory'
    id_item = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(250), nullable=False)
    product = db.Column(db.String(250), nullable=False)
    picture = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(User)

    def serialize (self):
        return{
            "id_item": self.id_item,
            "catogory": self.category,
            "product": self.product,
            "picture": self.picture,
            "description": self.description,
            "price": self.price,
            "user_id":self.user_id 
            
            }

    def __init__(self, category, product, picture, description, price, user_id):
        self.category = category
        self.product = product
        self.picture = picture
        self.description = description
        self.price = price 
        self.user_id = user_id

    def __repr__(self):
        return f"{self.category}: {self.product}:{self.picture} :{self.description}: {self.price}: {self.user_id}"  