from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from flask_jwt_extended import create_access_token, jwt_required

db = SQLAlchemy()

#API sing in "POST"
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    type = db.Column(db.String(250), nullable=False)

    def serialize (self):
        return{
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            "address": self.address,
           
        }
    
    def __init__(self, name, last_name, email, address, password):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.password = password

            
        


#API inventory "POST"
class Inventory(db.Model):
    __tablename__ = 'inventory'
    id_item = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(250), nullable=False)
    product = db.Column(db.String(250), nullable=False)
    #picture = db.Column(db.BLOB)
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
            "user": self.user.name
            }
    

"""
class Scheduling(db.Model):
    __tablename__ = 'scheduling'
    id_scheduling = db.Column(db.Integer, primary_key=True)
    start_hour = db.Column(db.String(250), nullable=False)
    end_hour = db.Column(db.String(250), nullable=False)
    day = db.Column(db.String(250), nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #user = relationship(User)

    def serialize(self):
        return{
            "id_scheduling": self.id_scheduling,
            "start_hour": self.start_hour,
            "end_hour": self.end_hour,
            "day": self.day,


        }

   
class Order(db.Model):
    __tablename__ = 'order'
    id_order = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Integer, nullable=False)
    status_commit = db.Column(db.String(250), nullable=False)
    #user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    #user = relationship(User)
    
    def serialize(self):
        return{
            "id_order": self.id_order,
            "total_price": self.total_price,
            "status_commit": self.status_commit

        }


class Order_item(db.Model):
    __tablename__ = 'order_item'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    order = relationship(Order)
    inventory_id = Column(Integer, ForeignKey('inventory.id'), nullable=False)
    inventory = relationship(Inventory)

"""