from .base import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy import Float, DateTime


class Product(BaseModel):
    __tablename__ = "products"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float)
    quantity = Column(Float)
    receipt_id = Column(Integer, ForeignKey('check.id'), nullable=False)
