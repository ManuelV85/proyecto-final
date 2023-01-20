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
            "addres": self.address,
            "type": self.type
        }


#API inventory "POST"
class Inventory(db.Model):
    __tablename__ = 'inventory'
    id_item = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(250), nullable=False)
    product = db.Column(db.String(250), nullable=False)
    picture = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #user = db.relationship(User)

    def serialize (self):
        return{
            "id_item": self.id_item,
            "catogory": self.category,
            "product": self.product,
            "picture": self.picture,
            "description": self.description,
            "price": self.price
        }
    


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

"""
class OrderItem(Base):
    __tablename__ = 'orderitem'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    order = relationship(Order)
    inventory_id = Column(Integer, ForeignKey('inventory.id'), nullable=False)
    inventory = relationship(Inventory)

"""