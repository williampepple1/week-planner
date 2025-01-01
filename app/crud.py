from . import schemas
from sqlalchemy.orm import Session
from . import models

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = models.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_activity(db: Session, activity: schemas.ActivityCreate, user_id: int):
    db_activity = models.Activity(**activity.dict(), user_id=user_id)
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

def get_activities(db: Session, user_id: int):
    return db.query(models.Activity).filter(models.Activity.user_id == user_id).all()
