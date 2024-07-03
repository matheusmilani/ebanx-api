from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()


def create():
    global db
    db.create_all()


def initialize_database(app):
    global db
    db.init_app(app)
