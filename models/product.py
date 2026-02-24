from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, DateTime, Text
from sqlalchemy.sql import func
from database.base import Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "products"
    id = Column("id", Integer, primary_key=True, index=True)
    name = Column("name", String(100), nullable=False, index=True, unique=True)
    description = Column("description", Text, nullable=False)
    price = Column("price", Numeric(10, 2), nullable=False, index=True)
    stock = Column("stock", Integer, nullable=False)
    category_id = Column("category_id", Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="products")