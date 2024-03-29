from flask import *
from flask_restful import Resource,Api
app = Flask(__name__)
api = Api(app)
todos = {}
class TodoApi(Resource):
    def get(self, todo_id):
        return {todo_id:todos[todo_id]}
    def post(self, todo_id):
        todos[todo_id]=request.form['data']
        return {todo_id:todos[todo_id]}

api.add_resource(TodoApi,'/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)