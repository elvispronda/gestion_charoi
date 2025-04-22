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
    make: int
    model: int
    year: int
    plate_number: str
    mileage: float = 0.0
    engine_size: float
    vehicle_type:int
    vehicle_transmission:int
    vehicle_fuel_type:int
    vin:str
    color:str
    purchase_price:float
    purchase_date:datetime
    status: str = "available"

class VehicleCreate(VehicleBase):
    pass

class VehicleOut(VehicleBase):
    id: int
    registration_date:datetime

    class Config:
        orm_mode = True
#########################################################################################################################################
class DocumentVehiculeBase(BaseModel):
   doc_category_id: int
   vehicle_id:int
   issued_date:datetime
   expiration_date:datetime
   
class DocumentVehiculeCreate(DocumentVehiculeBase):
    pass

class DocumentVehiculeOut(DocumentVehiculeBase):
    id: int
    created_at:datetime

    class Config:
        orm_mode = True
#########################################################################################################################################

class GarageBase(BaseModel):
   nom_garage:str

class GarageCreate(GarageBase):
    pass

class GarageOut(GarageBase):
    id: int

    class Config:
        orm_mode = True
#########################################################################################################################################

class CategoryMaintenanceBase(BaseModel):
   cat_maintenance:str

class CategoryMaintenanceCreate(CategoryMaintenanceBase):
    pass

class CategoryMaintenanceOut(CategoryMaintenanceBase):
    id: int

    class Config:
        orm_mode = True
#########################################################################################################################################

class MaintenanceBase(BaseModel):
   category_maintenance_id: int
   vehicule_id:int
   garage_id:int
   maintenance_cost:float
   receipt:str
   maintenance_date:datetime

class MaintenanceCreate(MaintenanceBase):
    pass

class MaintenanceOut(MaintenanceBase):
    id: int
    created_at:datetime

    class Config:
        orm_mode = True
#########################################################################################################################################

class Base(BaseModel):
   vehicle_model:str

class Create():
    pass

class Out():
    id: int

    class Config:
        orm_mode = True
#########################################################################################################################################

class CategoryPanneBase(BaseModel):
   nom_panne: str

class CategoryPanneCreate(CategoryPanneBase):
    pass

class CategoryPanneOut(CategoryPanneBase):
    id: int

    class Config:
        orm_mode = True
#########################################################################################################################################

class PanneBase(BaseModel):
   vehicle_id:int
   category_panne_id:int
   description: str | None = None
   status: str
   panne_date:datetime
   
class PanneCreate(PanneBase):
    pass

class PanneOut(PanneBase):
    id: int
    created_at:datetime


    class Config:
        orm_mode = True
#########################################################################################################################################

class ReparationBase(BaseModel):
   panne_id: int
   cost: float
   receipt:str
   garage_id: int
   repair_date:datetime

class ReparationCreate(ReparationBase):
    pass

class ReparationOut(ReparationBase):
    id: int

    class Config:
        orm_mode = True
#########################################################################################################################################

