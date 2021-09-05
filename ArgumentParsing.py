# to do list: DELETE, GET, PUT, POST

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '..........'},
    'todo3': {'task': 'profit :)'},
}