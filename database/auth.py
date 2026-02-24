import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings
from database.base import Base
from models.product import Product
from models.user import User

engine = create_engine(settings.DATABASE_URL)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)


def hash_password(password: str) -> str:
    """Hash a password using bcrypt"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed: str) -> bool:
    """Verify a password against its hash"""
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed.encode("utf-8"),
    )


def create_user(email: str, password: str, name: str):
    """Create user in database with check existing user"""
    hashed_password = hash_password(password)
    with Session(autoflush=False, bind=engine) as db:
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            return False
        new_user = User(name=name, email=email, hashed_password=hashed_password)
        db.add(new_user)
        db.commit()
        return True


def authenticate_user(email: str, password: str) -> None | User:
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user


def get_all_products():
    """Получить все товары из базы данных"""
    with Session(autoflush=False, bind=engine) as db:
        products = db.query(Product).all()
        return products


def get_product_by_id(product_id: int):
    """Получить товар по его id. Возвращает None, если товар не найден."""
    with Session(autoflush=False, bind=engine) as db:
        product = db.query(Product).filter(Product.id == product_id).first()
        return product
