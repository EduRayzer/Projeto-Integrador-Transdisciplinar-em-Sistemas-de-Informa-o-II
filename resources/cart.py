from flask_restful import Resource, reqparse
from models import Cart, db

parser = reqparse.RequestParser()
parser.add_argument('user_id')
parser.add_argument('product_id')
parser.add_argument('quantity')

class CartResource(Resource):
    def post(self):
        args = parser.parse_args()
        cart_item = Cart(user_id=args['user_id'], product_id=args['product_id'], quantity=args['quantity'])
        db.session.add(cart_item)
        db.session.commit()
        return {'message': 'Item added to cart'}, 201
