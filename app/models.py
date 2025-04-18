from sqlalchemy import Column, Integer ,String ,Boolean ,Float ,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key = True)
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    published = Column(Boolean,server_default = 'TRUE', nullable = False)
    created_at = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
    owner_id  = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),nullable = False)
#########################################################################################################################################

class User(Base):
    __tablename__ ="users"
    id = Column(Integer,primary_key= True, nullable = False)
    username = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable =False, unique = True)
    password = Column(String, nullable = False)
    role = Column(String, nullable = False, default="driver")  # driver, admin
    created_at = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
#########################################################################################################################################

class Driver(Base):
    __table__="drivers"
    id =Column(Integer,primary_key=True, nullable=False)
    nom =Column(String,nullable=False)
    prenom =Column(String, nullable=False)
    adresse =Column(String,nullable=False)
    cni=Column(String, nullable=False, unique=True)
    telephone =Column(String, nullable=False, unique=True)
    email =Column(String, nullable=False, unique=True)
    matricule =Column(String, nullable=False, unique=True)
#########################################################################################################################################

class CategoryFuel():
    __tablename__="category_fuel"
    id=Column(Integer,primary_key=True,index=True)
    fuel_category=Column(String,nullable=False) # e.g., fuel: Mzzout or essance
#########################################################################################################################################

class Fuel(Base):
    __tablename__ = "fuel"
    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    category_fuel = Column(Integer,ForeignKey("category_fuel.id")) 
    quantity = Column(Float, nullable=False)
    cost = Column(Float, nullable=False)
    date = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
 #########################################################################################################################################

class Maintenance(Base):
    __tablename__="maintenances"
    id =Column(Integer, primary_key=True, index=True)
    vehicle_id =Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    description =Column(String, nullable=False)
    cost =Column(Float, nullable=False)
    maintenance_date =Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
#########################################################################################################################################

class Trip(Base):
    __tablename__ = "trips"
    id =Column(Integer, primary_key=True, index=True)
    origin =Column(String, nullable=False)
    destination =Column(String, nullable=False)
    departure_date =Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()')) 
    return_date =Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
    vehicle_id =Column(Integer, ForeignKey("vehicles.id"))
    driver_id =Column(Integer, ForeignKey("users.id"))
#########################################################################################################################################

class Vehicle(Base):
    __tablename__= "vehicles"
    id =Column(Integer, primary_key=True, index=True)
    make =Column(String, nullable=False)
    model =Column(String, nullable=False)
    year =Column(Integer)
    plate_number =Column(String, unique=True, nullable=False)
    mileage =Column(Float, default=0.0)
    cost =Column(Float, default=0.0)
    status =Column(String, default="available")  # available, in_use, maintenance 
    starting_date=Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
#########################################################################################################################################

class CategoryDocument():
    __tablename__="category_document"
    id=Column(Integer,primary_key=True, index=True)
    doc_category=Column(String, nullable=False)
    cost=Column(Float, default=0.0)
#########################################################################################################################################

class DocumentVehicule():
    __tablename__="document_vehicule"
    id =Column(Integer,primary_key=True, index=True)
    category_id=Column(Integer,ForeignKey("category_document.id"))
    vehicule_id=Column(Integer,ForeignKey("vehicles.id"))
    issued_date=Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
    expiration_date=Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
#########################################################################################################################################

class Garage():
    __tablename__="garage"
    id=Column(Integer,primary_key=True, index=True)
    nom_garage=Column(String, nullable=False)
#########################################################################################################################################

class CategoryMaintenance():
    __tablename__="category_maintenance"
    id=Column(Integer,primary_key=True, index=True)
    maint_category=Column(String, nullable=False)
#########################################################################################################################################

class Maintenance():
    __tablename__="maintenance"
    id =Column(Integer,primary_key=True, index=True)
    category_maintenance_id=Column(Integer,ForeignKey("category_maintenance.id"))
    vehicule_id=Column(Integer,ForeignKey("vehicles.id"))
    garage_id=Column(Integer,ForeignKey("garage.id"))
    maintenance_cost=Column(Float, default=0.0)
    receipt=Column(String,nullable=False)
    maintenance_date=Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))   
#########################################################################################################################################

class CategoryPanne():
    __tablename__="category_panne"
    id=Column(Integer,primary_key=True, index=True)
    nom_panne=Column(String, nullable=False)
#########################################################################################################################################

class Panne():
    __tablename__="panne"
    id=Column(Integer, primary_key=True, index=True)
    vehicle_id=(Integer, ForeignKey("vehicles.id"))
    category_panne_id=Column(Integer, ForeignKey("category_panne.id"))
    description=Column(String,nullable=False)
    status=Column(String,default="active") #Active,Repaired
    panne_date=Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))   
#########################################################################################################################################

class Reparation():
    __tablename__="reparation"
    id=Column(Integer, ForeignKey=True,index=True)
    panne_id=Column(Integer, ForeignKey("panne.id"))
    cost=Column(Float,default=0.00)
    receipt=Column(String,nullable=False)
    garage_id=Column(Integer,ForeignKey("garage.id"))
    repair_date=Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
    status=Column(String,default="In progress ...") #In progress....,Completed
##########################################################################################################################################