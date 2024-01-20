from flask_restful import Resource


from ..models.db import db
from ..models.item import Product, Merchant, Listing, Barcode


class ItemList(Resource):
    def get(self):
        return {"data": [product.as_dict() for product in Product.query.all()]}


class Item(Resource):
    def get(self, id: int):
        return {"data": db.get_or_404(Product, id).as_dict()}
