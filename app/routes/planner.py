from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database, auth

router = APIRouter()

@router.post("/activities/")
def add_activity(activity: schemas.ActivityCreate, db: Session = Depends(database.get_db), current_user = Depends(auth.get_current_user)):
    return crud.create_activity(db=db, activity=activity, user_id=current_user.id)

@router.get("/activities/")
def list_activities(db: Session = Depends(database.get_db), current_user = Depends(auth.get_current_user)):
    return crud.get_activities(db=db, user_id=current_user.id)
