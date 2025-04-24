from fastapi import FastAPI,Response, status, HTTPException, Depends, APIRouter
from typing import Optional,List, Dict 
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import models ,schemas,oauth2,utils
from ..database import  get_db

router = APIRouter(prefix="/user", tags=['User'])

############################################################################################################################
@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut) 
def create_user(user : schemas.UserCreate, db:Session = Depends(get_db)):
    
    # Hash the password   _ user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

############################################################################################################################

@router.get("/", response_model = List[schemas.UserOut])
def get_users(db:Session = Depends(get_db), current_user : str = Depends(oauth2.get_current_user),
              limit : int = 5, skip : int = 0, search :Optional[str] = ""):
              
  
    ##filter all users at the same time
    users = db.query(models.User).filter(models.User.email.contains(search)).limit(limit).offset(skip).all()
    return users 
############################################################################################################################

@router.get("/{id}", response_model=schemas.TripOut)
def get_trip(id : int, db :Session = Depends(get_db),  current_user : str = Depends(oauth2.get_current_user)):
    trip = db.query(models.Trip).filter(models.Trip.id == id).first()
    
    if not trip :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Trip with id : {id} was not found")
    return trip

#############################################################################################################################

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_trip(id:int,db:Session = Depends(get_db), current_user : str = Depends(oauth2.get_current_user)):
   
   trip_query = db.query(models.Trip).filter(models.Trip.id == id)
   trip = trip_query.first()
   
   if trip == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Trip with id: {id} does not exist")
  
         
   trip_query.delete(synchronize_session = False) 
   db.commit()  
   return Response(status_code=status.HTTP_204_NO_CONTENT)
############################################################################################################################

@router.put("/{id}", response_model=schemas.TripCreate)
def update_trip(id:int,updated_trip:schemas.TripCreate,db:Session = Depends(get_db), current_user : str = Depends(oauth2.get_current_user)):
    
  
    trip_query = db.query(models.Trip).filter(models.Trip.id == id)
    trip =trip_query.first()
    if trip == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Trip with id: {id} does not exist")
   
    trip_query.update(updated_trip.dict(),synchronize_session = False)
    db.commit()
    return trip_query.first()  
############################################################################################################################

