from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

#API inventory "POST"
class Inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(250), nullable=False)
    product = db.Column(db.String(250), nullable=False)
    picture = db.Column(db.String(250), nullable=False)
    product = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    price = db.Column(db.float(250), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    """
   
"""
class Scheduling(Base):
    __tablename__ = 'scheduling'
    id = Column(Integer, primary_key=True)
    start_hour = Column(String(250), nullable=False)
    end_hour = Column(String(250), nullable=False)
    day = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
   
class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    total_price = Column(float(250), nullable=False)
    status = Column(String(250), nullable=False)
    paymentmethod_id = Column(Integer, ForeignKey('paymentmethod.id'), nullable=False)


class OrderItem(Base):
    __tablename__ = 'orderitem'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    order = relationship(Order)
    inventory_id = Column(Integer, ForeignKey('inventory.id'), nullable=False)
    inventory = relationship(Inventory)
  
 
class Shoppingcar(Base):
    __tablename__ = 'shoppingcar'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    status = Column(String(250), nullable=False)
    inventory_id = Column(Integer, ForeignKey('inventory.id'), nullable=False)
    inventory = relationship(Inventory)


class PaymentMethod(Base):
    __tablename__ = 'paymentmethod'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    payment_type = Column(String(250), nullable=False)
    transaction = Column(String(250), nullable=False)
    amount_transaction = Column(float(250), nullable=False)

"""