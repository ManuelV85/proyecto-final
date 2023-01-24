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
    id = db.Column(db.String(100), primary_key=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    #type = db.Column(db.String(250), nullable=False)

    def serialize (self):
        return{
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "address": self.address,
           
        }
    
    def __init__(self, first_name, last_name, email, address, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.password = password