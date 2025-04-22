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
#########################################################################################################################################

class DriverBase(BaseModel):
    nom: str
    prenom: str
    cni: str
    email: str
    matricule:str
   
class BudgetCreate(DriverBase):
    pass

class BudgetOut(DriverBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
#########################################################################################################################################
class CategoryFuelBase(BaseModel):
    fuel_category: str
    

class CategoryFuelCreate(CategoryFuelBase):
    pass

class FuelLogOut(CategoryFuelBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

#########################################################################################################################################

class FuelBase(BaseModel):
    vehicle_id: int
    category_fuel_id: int
    quantity:float
    cost: float

class FuelLogCreate(FuelBase):
    pass

class FuelLogOut(FuelBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

#########################################################################################################################################

class MaintenanceBase(BaseModel):
    category_maintenance_id: int
    vehicule_id: int
    garage_id: int
    maintenance_cost: float
    # description: str | None = None
    receipt: str
    

class MaintenanceCreate(MaintenanceBase):
    pass

class MaintenanceOut(MaintenanceBase):
    id: int
    maintenance_date: date

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
# class UserBase(BaseModel):
#     username: str
#     full_name: str
#     email: EmailStr

# class UserCreate(UserBase):
#     password: str

# class UserOut(UserBase):
#     id: int
#     role: str

#     class Config:
#         orm_mode = True

# class UserLogin(BaseModel):
#     username: str
#     password: str

#########################################################################################################################################
class VehicleTransmissionBase(BaseModel):
    vehicle_transmission:str

class VehicleTransmissionCreate(VehicleTransmissionBase):
    pass

class VehicleTransmissionOut(VehicleTransmissionBase):
    id: int

    class Config:
        orm_mode = True
#########################################################################################################################################

class VehicleFuelTypeBase(BaseModel):
   fuel_type:str

class VehicleFuelTypeCreate(VehicleFuelTypeBase):
    pass

class VehicleFuelTypeOut(VehicleFuelTypeBase):
    id: int

    class Config:
        orm_mode = True
#########################################################################################################################################

class VehicleTypeBase(BaseModel):
   vehicle_type:str

class VehicleTypeCreate(VehicleTypeBase):
    pass

class VehicleTypeOut(VehicleTypeBase):
    id: int

    class Config:
        orm_mode = True
#########################################################################################################################################

class VehicleMakeBase(BaseModel):
    vehicle_make:str

class VehicleMakeCreate(VehicleMakeBase):
    pass

class VehicleMakeOut(VehicleMakeBase):
    id: int

    class Config:
        orm_mode = True
#########################################################################################################################################

class VehicleModelBase(BaseModel):
   vehicle_model:str

class VehicleModelCreate():
    pass

class VehicleModelOut():
    id: int

    class Config:
        orm_mode = True
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


