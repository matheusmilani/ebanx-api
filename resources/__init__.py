from datetime import datetime, timedelta
from flask import jsonify, current_app, request
from flask_jwt_simple import JWTManager, get_jwt
from flask_restful import Api
from flask_cors import CORS
from functools import wraps
from werkzeug.exceptions import HTTPException
from os import environ
from dotenv import load_dotenv
import json
import jwt
import requests

def initialize_resources(application):
    api = Api(application)
    jwt = JWTManager(application)
    CORS(application, supports_credentials=True, origins="*")

    from resources.balance_resource import BalanceResource
    from resources.event_resource import EventResource
    from resources.reset_resource import ResetResource

    api.add_resource(BalanceResource, '/balance')
    api.add_resource(EventResource, '/event')
    api.add_resource(ResetResource, '/reset')

    @application.errorhandler(Exception)
    def handle_error(e):
        code = 500
        if isinstance(e, HTTPException):
            code = e.code
        if environ.get('EBS_ENVIRONMENT') in ['local', None]:
            return jsonify(message=str(e)), code
        return jsonify(message='error'), code

    @application.after_request
    def nocache_control(response):
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE'
        response.headers['Access-Control-Allow-Origin'] = '*'

        return response

def authorize():
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if 'Authorization' not in request.headers:
                return {'message':'Missing authorization header'}, 403
            return f(*args, **kwargs)
        return wrapped
    return wrapper
