from flask_restful import Resource
from flask import request


from ..models.db import db
from ..models.item import Product, Merchant, Listing, Barcode


class ItemList(Resource):
    def get(self):
        return {"data": [product.as_dict() for product in Product.query.all()]}


class Item(Resource):
    def get(self, id: int):
        return {"data": db.get_or_404(Product, id).as_dict()}


class SearchItems(Resource):
    def get(self):
        query_string = request.args.get('q')
        page = request.args.get('page', default=1, type=int)
        per_page = 30  # Number of items per page
        start = request.args.get("start", type=float)
        end = request.args.get("end", type=float)
        # Calculate the offset based on the page number
        offset = (page - 1) * per_page

        if query_string:
            if start != None:
                sql = Product.query.join(Listing, Product.listings).filter(Product.name.ilike(f"%{query_string}%")).filter(
                    Listing.price.between(start, end)).order_by(
                    Listing.price)
                products = sql.offset(offset).limit(per_page).all()
            else:
                sql = Product.query.join(Listing, Product.listings).filter(Product.name.ilike(f"%{query_string}%")).order_by(
                    Listing.price)
                products = sql.offset(offset).limit(per_page).all()

        else:
            if start != None:
                sql = Product.query.join(Listing, Product.listings).filter(
                    Listing.price.between(start, end)).order_by(
                    Listing.price)
                products = sql.offset(offset).limit(per_page).all()
            else:
                sql = Product.query.join(Listing, Product.listings).order_by(
                    Listing.price)
                products = sql.offset(offset).limit(per_page).all()

        # Convert the list of products to a list of dictionaries
        data = [product.as_dict() for product in products]
        return {
            "data": data,
            "page": page,
            "per_page": per_page,
            # "total_results": Product.query.filter(Product.name.ilike(f"%{query_string}%")).count() if query_string else Product.query.count()
            "total_results": sql.count()
        }
