from flask_restful import Resource


class ItemList(Resource):
    def get(self):
        return {"msg": "hello world"}
