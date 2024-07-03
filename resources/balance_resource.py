from flask import request
from flask_jwt_simple import create_jwt
from flask_restful import Resource
from helpers import *
from models.account import Account

from resources import authorize
import re

class BalanceResource(Resource):

    def get(self):
        if 'account_id' in request.args:
            account = Account.get(request.args['account_id'])
            if isNoneOrZero(account):
                return 0, 404
            return account.balance, 200
        return 0, 404