from flask_restful import Resource, reqparse
from models import User, db
from werkzeug.security import generate_password_hash, check_password_hash

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')

class AuthResource(Resource):
    def post(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return {'message': 'Login successful'}, 200
        return {'message': 'Invalid credentials'}, 401
