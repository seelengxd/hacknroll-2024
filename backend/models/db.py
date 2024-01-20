from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import random
import click


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def add_db_setup_commands(app: Flask):
    from .item import Product, Merchant, Listing, Barcode

    def init_db():
        with app.app_context():
            db.create_all()

    def seed_db():
        """Insert dummy data."""
        # 2 products
        # 1 has a barcode
        # 4 listings
        # 2 merchants

        Listing.query.delete()
        Barcode.query.delete()
        Product.query.delete()
        Merchant.query.delete()

        product_a = Product(name="A", brand="brand A",
                            description="desc 1", image_url="www.url.com", size="whatever")
        product_b = Product(name="B", brand="brand B",
                            description="desc 2", image_url="www.url.com", size="whatever")
        products = [product_a, product_b]

        merchant_a = Merchant(name="NTUC")
        merchant_b = Merchant(name="Cold Storage")
        merchants = [merchant_a, merchant_b]

        listings = []
        for product in products:
            for merchant in merchants:
                listing = Listing(
                    price=round(random.random() * 10, 2), url_to_product="www.whatever.com")
                listing.merchant = merchant
                listing.product = product
                listings.append(listing)

        product_a.barcodes.append(Barcode(value="a barcode."))

        db.session.add_all(merchants + products + listings)
        db.session.commit()

    @app.cli.command("init-db")
    def init_db_command():
        init_db()
        click.echo("Initialised the database.")

    @app.cli.command("seed-db")
    def seed_db_command():
        seed_db()
        click.echo("Seeded the database.")
