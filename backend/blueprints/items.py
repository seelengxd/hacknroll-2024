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
    # attendance_records = (db.session.query(LargeGroupAttendance).
    # filter_by(large_group_id = event_id).
    # join(Attendee, LargeGroupAttendance.attendee).
    # order_by(desc(Attendee.first_name))
    # )
    def get(self):
        query_string = request.args.get('q')
        page = request.args.get('page', default=1, type=int)
        per_page = 30  # Number of items per page
        # Calculate the offset based on the page number
        offset = (page - 1) * per_page
        if query_string:
            products = Product.query.filter(Product.name.ilike(f"%{query_string}%")).join(Listing, Product.listings).order_by(
                Listing.price).offset(offset).limit(per_page).all()
        else:
            products = Product.query.join(Listing, Product.listings).order_by(
                Listing.price).offset(offset).limit(per_page).all()

        # Convert the list of products to a list of dictionaries
        data = [product.as_dict() for product in products]
        return {
            "data": data,
            "page": page,
            "per_page": per_page,
            "total_results": Product.query.filter(Product.name.ilike(f"%{query_string}%")).count() if query_string else Product.query.count()
        }
