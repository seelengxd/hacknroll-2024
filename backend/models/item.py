from .db import db
from typing import Optional, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Product(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    brand: Mapped[str]
    description: Mapped[Optional[str]]
    image_url: Mapped[str]
    barcode: Mapped[int] = mapped_column(unique=True)
    size: Mapped[str] = mapped_column()

    listings: Mapped[List["Listing"]] = relationship(back_populates="product")


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
    url_to_product: Mapped[str]

    product: Mapped[Product] = relationship(back_populates="listings")
    merchant: Mapped[Merchant] = relationship(back_populates="listings")
