from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base  # Import the Base from database.py
from datetime import datetime, timedelta

class User(Base):  # Use the same Base
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)

class Activity(Base):  # Use the same Base
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    is_completed = Column(Boolean, default=False)
    deadline = Column(DateTime, default=lambda: datetime.now() + timedelta(days=7))
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="activities")

User.activities = relationship("Activity", back_populates="user")
