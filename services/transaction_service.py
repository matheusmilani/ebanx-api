from models.account import Account

from helpers import *

class TransactionService():
    def __init__(self):
        return
    
    def deposit(self, destination, amount):
        try:
            account = Account.get(destination)
            if isNoneOrZero(account):
                item = Account()
                item.id = destination
                item.balance = amount
                item.save()
                return item.balance
            account.balance += amount
            account.update()
            return account.balance
        except:
            return "error"

    def withdraw(self, origin, amount):
        try:
            account = Account.get(origin)
            if isNoneOrZero(account) != None and amount <= account.balance:
                account.balance -= amount
                account.update()
                return account.balance
            return "error"
        except:
            return "error"
    
    def transfer(self, origin, amount, destination):
        try:
            origin_account = Account.get(origin)
            destination_account = Account.get(destination)
            if self.withdraw(origin, amount) != "error":
                self.deposit(destination, amount)
                return [origin_account.balance, Account.get(destination).balance]
            return []
        except:
            return "error"