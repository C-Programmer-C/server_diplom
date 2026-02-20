from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
from models.user import User
import bcrypt



engine = create_engine(settings.DATABASE_URL)
Session = sessionmaker(bind=engine)


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

def find_user(email: str, password: str):
    with Session(autoflush=False, bind=engine) as db:
        existing_user = db.query(User).filter(User.email == email, User.password == password).first()
        if not existing_user:
            return False
    return True