from models import db
from sqlalchemy import create_engine

class Schema:
    @staticmethod
    def migration():
        db.configure_mappers()
        db.create_all()

    def prepare_db():
        return
