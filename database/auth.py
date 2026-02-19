from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
from sqlalchemy.orm import declarative_base
from passlib.context import CryptContext
from models.user import User


Base = declarative_base()
engine = create_engine(settings.DATABASE_URL)
Session = sessionmaker(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(email: str, password: str, name: str):
    hashed_password = pwd_context.hash(password)
    with Session(autoflush=False, bind=engine) as db:
        existing_user = db.query(User).filter(User.email == email).first
        if (existing_user):
            return False
        new_user = User(name=name, email=email, hashed_password=hashed_password)
        db.add(new_user)
        db.commit()
        return True