import sys

sys.path.insert(0, 'models')
sys.path.insert(1, 'core')
from Todo import *
from TodoService import *
from flask import Flask
from flask_restful import Resource, Api
import json
from flask import request

choice = " "

# instantiation
todoService = TodoService()

app = Flask(__name__)
api = Api(app)


class TodoApi(Resource):

    def delete(self):
        json_data = request.get_json(force=True)
        idx = json_data['idx']
        todoService.delete(idx)
        return "delete done!"

    def put(self):
        json_data = request.get_json(force=True)
        desc = json_data['desc']
        idx = json_data['idx']
        todoService.update(desc, idx)
        return "update done!"

    def post(self):
        json_data = request.get_json(force=True)
        desc = json_data['desc']
        todoService.create(desc)
        return "done!"

    def get(self):
        lst = todoService.retrieve()
        return json.dumps([ob.__dict__ for ob in lst])


api.add_resource(TodoApi, '/mika')

if __name__ == '__main__':
    app.run(debug=True)
