from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import datetime
from typing import Optional, Union
from datetime import date

   
class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True
    

class PostCreate(PostBase):
    pass

class Userout(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime
    
    class config :
        orm_mode = True
        
        
class Post(PostBase):
    id : int
    created_at : datetime
    owner_id : int
    owner : Userout
    
    class config :
        orm_mode = True
        
class PostOut(PostBase):
    Post : Post
    votes : int    

class UserCreate(BaseModel):
    email : EmailStr
    password : str
    
       
class UserLogin(BaseModel):
    email : EmailStr
    password : str
    
class Token(BaseModel):
    access_token : str
    token_type : str
    

class TokenData(BaseModel):
    id: Union[str, int]  # Accepts both string and integer types



# class Vote(BaseModel):
#     post_id : int
#     dir : conint(le=1) # type: ignore








class BudgetBase(BaseModel):
    category: str
    amount: float
    date: date
    description: str | None = None
    vehicle_id: int

class BudgetCreate(BudgetBase):
    pass

class BudgetOut(BudgetBase):
    id: int

    class Config:
        orm_mode = True
#########################################################################################################################################
class FuelLogBase(BaseModel):
    vehicle_id: int
    quantity: float
    cost: float

class FuelLogCreate(FuelLogBase):
    pass

class FuelLogOut(FuelLogBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True

#########################################################################################################################################

class FuelLogBase(BaseModel):
    vehicle_id: int
    date: date
    fuel_type: str
    volume: float
    cost: float

class FuelLogCreate(FuelLogBase):
    pass

class FuelLogOut(FuelLogBase):
    id: int

    class Config:
        orm_mode = True

#########################################################################################################################################

class MaintenanceBase(BaseModel):
    vehicle_id: int
    description: str
    cost: float
    maintenance_date: date

class MaintenanceCreate(MaintenanceBase):
    pass

class MaintenanceOut(MaintenanceBase):
    id: int

    class Config:
        orm_mode = True
#########################################################################################################################################
class TripBase(BaseModel):
    origin: str
    destination: str
    departure_date: date
    return_date: date | None = None
    vehicle_id: int
    driver_id: int

class TripCreate(TripBase):
    pass

class TripOut(TripBase):
    id: int

    class Config:
        orm_mode = True

#########################################################################################################################################
class UserBase(BaseModel):
    username: str
    full_name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

#########################################################################################################################################
class VehicleBase(BaseModel):
    make: str
    model: str
    year: int
    plate_number: str
    mileage: float = 0.0
    status: str = "available"

class VehicleCreate(VehicleBase):
    pass

class VehicleOut(VehicleBase):
    id: int

    class Config:
        orm_mode = True


