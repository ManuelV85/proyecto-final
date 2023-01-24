from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
"""



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
    addres_ws_store = db.Column(db.String(250), nullable = False)
    scheduling_ws_store = db.Column(db.String(250), nullable = False)

def serialize (self):
    return {
        "id_ws": self.id_ws,
        "name_ws_store" : self.name_ws_store,
    }



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
        self.description = description
        self.price = price 
        self.user_id = user_id

    def __repr__(self):
        return f"{self.category}: {self.product}: {self.description}: {self.price}: {self.user_id}"   
