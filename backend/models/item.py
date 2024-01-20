from .db import db
from typing import Optional, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Barcode(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(
        ForeignKey("product.id"))
    value: Mapped[str]

    product: Mapped["Product"] = relationship(back_populates="barcodes")


class Product(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    brand: Mapped[str]
    description: Mapped[Optional[str]]
    image_url: Mapped[str]
    size: Mapped[str]

    listings: Mapped[List["Listing"]] = relationship(back_populates="product")
    barcodes: Mapped[List[Barcode]] = relationship(back_populates="product")


class Merchant(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    listings: Mapped[List["Listing"]] = relationship(back_populates="merchant")


class Listing(db.Model):
    product_id: Mapped[int] = mapped_column(
        ForeignKey("product.id"), primary_key=True)
    merchant_id: Mapped[int] = mapped_column(
        ForeignKey("merchant.id"), primary_key=True)
    price: Mapped[float]
    offer_qty: Mapped[Optional[int]]
    offer_price: Mapped[Optional[float]]
    offer_display: Mapped[Optional[str]]
    url_to_product: Mapped[str]

    product: Mapped[Product] = relationship(back_populates="listings")
    merchant: Mapped[Merchant] = relationship(back_populates="listings")
