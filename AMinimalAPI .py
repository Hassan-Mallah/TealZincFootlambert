from flask import Flask
from flask_restful import  Resource, Api

# Using __name__ isn't orthogonal to "hardcoding", it's just a shortcut to using the name of the package
app = Flask(__name__)
api = Api(app)


class HelooWorld(Resource):
    def get(self):
        return {'hello': 'world'}


# connect a link to the class
api.add_resource(HelooWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)