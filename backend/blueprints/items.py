from flask_restful import Resource


class ItemList(Resource):
    def get(self):
        return {"msg": "hello world"}


class Item(Resource):
    def get(self):
        pass
