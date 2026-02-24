# seed.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.category import Category
from models.product import Product
from models.user import User
from config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

if not session.query(Category).first():
    categories = [
        Category(name="Электроника"),
        Category(name="Книги"),
        Category(name="Одежда"),
    ]
    session.add_all(categories)
    session.commit()

    products = [
        Product(name="Смартфон", description="...", price=19999.99, stock=10, category_id=categories[0].id),
        Product(name="Ноутбук", description="...", price=54999.99, stock=5, category_id=categories[0].id),
    ]
    session.add_all(products)
    session.commit()
    print("Данные были успешно добавлены")
else:
    print("Данные уже существуют, пропускаем вставку.")

session.close()