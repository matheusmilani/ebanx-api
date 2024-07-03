from datetime import datetime
from models import db

class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)

    balance = db.Column(db.Integer, primary_key=False)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    @staticmethod
    def get(id :int):
        return Account.query.filter_by(id=id).first()

    @staticmethod
    def list():
        return Account.query.all()

    def save(self):
        self.created_at = datetime.now()
        self.last_login_at = datetime.now()
        db.session.merge(self)
        db.session.commit()

    def update(self):
        self.updated_at = datetime.now()
        db.session.merge(self)
        db.session.commit()
    
    @staticmethod
    def delete(id :int):
        Account.query.filter_by(id=id).delete()
        db.session.commit()
    
    @staticmethod
    def delete_all():
        Account.query.delete()
        db.session.commit()