from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class ActivityBase(BaseModel):
    title: str
    is_completed: bool = False

class ActivityCreate(ActivityBase):
    pass

class Activity(ActivityBase):
    id: int
    deadline: datetime
    user_id: int

    class Config:
        from_attributes = True
