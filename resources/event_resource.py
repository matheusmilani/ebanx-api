from flask import request
from flask_jwt_simple import create_jwt
from flask_restful import Resource
from helpers import *
from models.account import Account

from resources import authorize
from services.transaction_service import TransactionService
from enum import *
import re


class EventResource(Resource):

    def post(self):
        data = request.get_json()
        transaction = TransactionService()

        if 'origin' in data and isNoneOrZero(Account.get(data['origin'])):
            return 0, 404

        match data['type']:
            case 'deposit':
                return self.deposit_process(transaction, data)
            case 'withdraw':
                return self.withdraw_process(transaction, data)
            case 'transfer':
                return self.transfer_process(transaction, data)
            case _:
                return 0, 404
        return 0, 404
    
    def deposit_process(self, transaction, data):
        balance = transaction.deposit(data['destination'], data['amount'])
        if balance == "error":
            return 0, 404
        return {"destination": {"id": data['destination'], "balance": balance}}, 201
    
    def withdraw_process(self, transaction, data):
        if data['amount'] > Account.get(data['origin']).balance:
            return 0, 404
        balance = transaction.withdraw(data['origin'], data['amount'])
        if balance == "error":
            return 0, 404
        return {"origin": {"id": data['origin'], "balance": balance}}, 201
    
    def transfer_process(self, transaction, data):
        balances = transaction.transfer(data['origin'], data['amount'], data['destination'])
        if balances == "error":
            return 0, 404
        return {"origin": {"id": data['origin'], "balance": balances[0]}, "destination": {"id": data['destination'], "balance":balances[1]}}, 201