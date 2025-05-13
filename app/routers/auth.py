from fastapi import FastAPI,Response, status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..schemas import UserLogin
from .. import database, oauth2, schemas, models, utils 


"""router = APIRouter(tags=['Authentification'])
 @router.post('/login', response_model=schemas.Token)
def login(user_credentials : OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = f"Invalid credentials")
    
    access_token = oauth2.create_access_token(data = {"user_id" :user.id})
    return {"access_token": access_token, "token_type" : "bearer"} """


#There is a difference when using form data or json format

router = APIRouter(tags=['Authentification'])
@router.post('/login', response_model=schemas.Token)
def login(user_credentials: UserLogin, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()  # Change username to email
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    if not utils.verify(user_credentials.password, user.password):  # Verify password
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})  # Generate the access token
    
    return {"access_token": access_token, "token_type": "bearer"}  # Return the token and token type







