from flask import Flask, request
from flask_restful import  Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodSimple(Resource):
    def get(self, todo_id=None):
        if todo_id is None:
            return todos
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


api.add_resource(TodSimple, '/', endpoint='todos') # to show list
api.add_resource(TodSimple, '/<string:todo_id>', endpoint='todo') # to show 1 item or put

if __name__ == '__main__':
    app.run(debug=True)