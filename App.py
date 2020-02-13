import sys

sys.path.insert(0, 'models')
sys.path.insert(1, 'core')
from Todo import *
from TodoService import *
from flask import Flask
from flask_restful import Resource, Api


choice = " "
todoService = TodoService()

app = Flask(__name__)
api = Api(app)


class WebApp(Resource):
    def get(self):
        t = Todo()
        t.desc = "yaay!"
        return t.__dict__


api.add_resource(WebApp, '/')

if __name__ == '__main__':
    app.run(debug=True)
