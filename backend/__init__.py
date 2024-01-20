from flask import Flask
from flask_cors import CORS

from .models.db import db, add_db_setup_commands

from .blueprints.items import ItemList, Item
from flask_restful import Api


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://postgres:postgres@localhost:5432/items")

    db.init_app(app)
    add_db_setup_commands(app)

    api = Api(app)

    api.add_resource(ItemList, "/items")
    api.add_resource(Item, "/items/<int:id>")

    return app
