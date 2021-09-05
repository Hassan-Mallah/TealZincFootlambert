# to do list: DELETE, GET, PUT, POST
# example
# Todos list: curl http://127.0.0.1:5000/
# PUT add or update a task: curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
# show a task:  curl http://localhost:5000/todo1
# delete a task: curl http://localhost:5000/todos/todo3 -X delete -v
# POST add a new task: curl http://localhost:5000/todos -d "task=something new new" -X post -v

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '..........'},
    'todo3': {'task': 'profit :)'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} not found".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')  # add validation to task variable


# returns single to do item, and lets your delete an item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    # requires task id and text
    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# returns list of list of Tasks, POST
class TodoList(Resource):
    def get(self):
        return TODOS

    # requires only task text
    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1  # id of next item
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return  TODOS[todo_id], 201


api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(TodoList, '/todos')

if __name__ == '__main__':
    app.run(debug=True)