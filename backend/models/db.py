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

        import json
        with open("whatever.json") as f:
            data = json.load(f)

        # product_a = Product(name="A", brand="brand A",
        #                     description="desc 1", image_url="www.url.com", size="whatever")
        # product_b = Product(name="B", brand="brand B",
        #                     description="desc 2", image_url="www.url.com", size="whatever")
        # products = [product_a, product_b]

#   {
#     "product_url": "https://www.fairprice.com.sg/product/555-premium-stainless-steel-deep-rice-plate-16cm-1-pc-90114695",
#     "market_id": 1,
#     "barcodes": ["8888310126168"],
#     "brand": "555",
#     "price": 5.04,
#     "availability": false,
#     "name": "555 Premium Stainless Steel Deep Rice Plate 16cm",
#     "image": "https://media.nedigital.sg/fairprice/fpol/media/images/product/XL/90114695_XL1_20230210.jpg",
#     "quantity": "1 pc",
#     "offer_qty": null,
#     "offer_price": null,
#     "offer_desc": null,
#     "treated_brand": "555",
#     "key": ["555", 26]
#   },
        count = 1
        merchant_a = Merchant(id=1, name="NTUC")
        merchant_b = Merchant(id=2, name="Cold Storage")
        merchant_c = Merchant(id=3, name="Sheng Shiong")

        merchants = [merchant_a, merchant_b, merchant_c]

        products = []
        listings = []
        for product in data:
            product["key"] = tuple(product["key"])

        processed = {}
        for product in data:
            if product["key"] not in processed:
                processed[product["key"]] = [product]
            else:
                processed[product["key"]].append(product)

        for k, v in processed.items():
            first = v[0]
            name = first["name"]
            brand = first["brand"]
            image_url = first["image"] if first["image"] else ""
            size = first["quantity"] if first["quantity"] else ""
            product = Product(name=name, brand=brand,
                              image_url=image_url, size=size)
            for product_data in v:
                # CREATE LISTING
                merchant_id = product_data["market_id"]
                price = product_data["price"]
                if isinstance(price, str) and price[0] == "$":
                    if "/" in price:
                        price = price.split("/")[0].strip()
                    price = float(price[1:])
                offer_qty = product_data["offer_qty"]
                offer_price = product_data["offer_price"]
                if isinstance(offer_price, str) and offer_price[0] == "$":
                    if "/" in offer_price:
                        offer_price = offer_price.split("/")[0].strip()
                    offer_price = float(offer_price[1:])
                offer_desc = product_data["offer_desc"]
                url_to_product = product_data["product_url"]
                listing = Listing(id=count, merchant_id=merchant_id, price=price,
                                  offer_qty=offer_qty, offer_price=offer_price, offer_display=offer_desc, url_to_product=url_to_product)
                count += 1
                product.listings.append(listing)
            products.append(product)
            # v is related products.

            # for merchant in merchants:
            #     listing = Listing(
            #         price=round(random.random() * 10, 2), url_to_product="www.whatever.com")
            #     listing.merchant = merchant
            #     listing.product = product
            #     listings.append(listing)

        # product_a.barcodes.append(Barcode(value="a barcode."))

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
