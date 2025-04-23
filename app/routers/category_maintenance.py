from fastapi import FastAPI,Response, status, HTTPException, Depends, APIRouter
from typing import Optional,List, Dict 
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import models ,schemas,oauth2,utils
from ..database import  get_db

router = APIRouter(prefix="/category_maintenance", tags=['Category aintenance'])

############################################################################################################################
@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.CategoryMaintenanceOut) 
def create_cat_maintenance(cat_maintenance: schemas.CategoryMaintenanceCreate, db:Session = Depends(get_db)):
    
    new_cat_maintenance = models.CategoryMaintenance(**cat_maintenance.dict())
    db.add(new_cat_maintenance)
    db.commit()
    db.refresh(new_cat_maintenance)
    return new_cat_maintenance

############################################################################################################################

@router.get("/", response_model = List[schemas.CategoryMaintenanceOut])
def get_caat_maintenance(db:Session = Depends(get_db), current_user : str = Depends(oauth2.get_current_user),
              limit : int = 5, skip : int = 0, search :Optional[str] = ""):
              
  
    ##filter all maintenance categories at the same time
    maintenance_categories = db.query(models.CategoryMaintenance).filter(models.CategoryMaintenance.cat_maintenance.contains(search)).limit(limit).offset(skip).all()
    return maintenance_categories
############################################################################################################################

@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id : int, db :Session = Depends(get_db),  current_user : str = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id : {id} was not found")
    return user

#############################################################################################################################

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int,db:Session = Depends(get_db), current_user : str = Depends(oauth2.get_current_user)):
   
   user_query = db.query(models.User).filter(models.User.id == id)
   user = user_query.first()
   
   if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} does not exist")
  
         
   user_query.delete(synchronize_session = False) 
   db.commit()  
   return Response(status_code=status.HTTP_204_NO_CONTENT)
############################################################################################################################

@router.put("/{id}", response_model=schemas.UserCreate)
def update_user(id:int,updated_user:schemas.UserCreate,db:Session = Depends(get_db), current_user : str = Depends(oauth2.get_current_user)):
    
  
    user_query = db.query(models.User).filter(models.User.id == id)
    user =user_query.first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} does not exist")
   
    user_query.update(updated_user.dict(),synchronize_session = False)
    db.commit()
    return user_query.first()  
############################################################################################################################