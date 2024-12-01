from flask_restful import Resource
from models import Product, db

class ProductsResource(Resource):
    def get(self):
        products = Product.query.all()
        return [{'id': p.id, 'name': p.name, 'description': p.description, 'price': p.price} for p in products], 200
