"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from random import randint

api = Blueprint('api', __name__)


class users_structure:
    def __init__(self, surname):
        self.surname = surname

        self.users = [{
            "name/WS_name": "Gokubike",
            "last_name": "",
            "e-mail": "vegita@vegetables.com",
            "password": "gar4gasd2",
            "addres": "somewhere",
            "id": self.generate_id()
        }
        {
            "name/WS_name": "Vegetta",
            "last_name": "Sayajin",
            "e-mail": "vegita@vegetables.com",
            "password": "gar4gasd2",
            "addres": "somewhere",
            "id": self.generate_id()

        }]

        def _generate_id():
            return randint ( 0,9999999999)