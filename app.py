from dotenv import load_dotenv
from flask import Flask
from models import initialize_database
from os import environ
from resources import initialize_resources
from schema.schema_file import Schema
from sqlalchemy import create_engine

application = Flask(__name__)

load_dotenv('./environments/local.env')

for item in environ.items():
    application.config[item[0]] = item[1]

initialize_database(application)
initialize_resources(application)

@application.before_first_request
def startup():
    print("Initializing migration DB")

    Schema.migration()
    Schema.prepare_db()

if __name__ == '__main__':
    application.run(threaded=True)
