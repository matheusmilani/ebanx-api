import pytest
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from . import create_test_app
from . import db
from services.transaction_service import *
from models.account import Account

@pytest.fixture(scope="session", autouse=True)
def before_all():
    create_test_app()
    Account().delete_all()

class TestService:
    def test_deposit_event(self):
        destination = 100
        amount = 10

        assert TransactionService().deposit(destination, amount) == 10
        assert TransactionService().deposit(destination, amount) == 20

    def test_withdraw_event(self):
        origin = 100
        amount = 5
        assert TransactionService().withdraw(origin, amount) == 15

        origin = 200
        assert TransactionService().withdraw(origin, amount) == 'error'

        origin = 100
        amount = 500
        assert TransactionService().withdraw(origin, amount) == 'error'

    def test_transfer_event(self):
        origin = 100
        amount = 15
        destination = 300
        assert TransactionService().transfer(origin, amount, destination) == [0, 15]

        origin = 200
        assert TransactionService().transfer(origin, amount, destination) == []

        destination = 300
        assert TransactionService().transfer(origin, amount, destination) == []
        
        Account().delete_all()
    
