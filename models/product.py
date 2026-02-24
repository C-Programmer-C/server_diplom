from sqlalchemy import Column, Integer, Numeric, String, DateTime, Text
from sqlalchemy.sql import func
from database.base import Base


class Product(Base):
    __tablename__ = "products"
    id = Column("id", Integer, primary_key=True, index=True)
    name = Column("name", String(100), nullable=False, index=True, unique=True)
    description = Column("description", Text, nullable=False)
    price = Column("price", Numeric(10, 2), nullable=False, index=True)
    stock = Column("stock", Integer, nullable=False)
    category = Column("category", String(100), nullable=False)
