from flask_sqlalchemy import SQLAlchemy

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    type = Column(String(250), nullable=False)

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True)
    category = Column(String(250), nullable=False)
    product = Column(String(250), nullable=False)
    picture = Column(String(250), nullable=False)
    product = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    price = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
   

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
    total_price = Column(String(250), nullable=False)
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
    amount_transaction = Column(String(250), nullable=False)