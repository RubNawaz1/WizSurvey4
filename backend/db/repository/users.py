from core.hashing import Hasher
from db.models.users import User
from schemas.users import UserCreate
from sqlalchemy.orm import Session

def home(db: Session):
    home = db.query(User).all()
    return home

def create_new_user(user: UserCreate, db: Session):
    user = User(
        userfirstname=user.userfirstname,
        userlastname=user.userlastname,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        status=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user
