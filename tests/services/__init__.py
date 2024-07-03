from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from schema.schema_file import Schema
from dotenv import load_dotenv
from os import environ
from models import initialize_database
from os import environ
from resources import initialize_resources
from models import db


def create_test_app():
    global app

    app = Flask(__name__)
    load_dotenv('./environments/test.env')
    for item in environ.items():
        app.config[item[0]] = item[1]
    app.app_context().push()

    initialize_database(app)
    initialize_resources(app)

    Schema.migration()
    Schema.prepare_db()
