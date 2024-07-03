from flask import request
from flask_jwt_simple import create_jwt
from flask_restful import Resource
from helpers import *
from models.account import Account
from resources import authorize
from services.transaction_service import TransactionService
from enum import *
import re


class ResetResource(Resource):

    def post(self):
        Account().delete_all()
        return 'OK', 200