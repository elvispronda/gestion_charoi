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
    owner = relationship("User")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key= True, nullable = False)
    username = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable =False, unique = True)
    password = Column(String, nullable = False)
    role = Column(String, nullable = False, default="driver")  # driver, admin
    created_at = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
 
    
class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id", ondelete ="CASCADE"), primary_key=True)
    post_id =  Column(Integer, ForeignKey("posts.id", ondelete ="CASCADE"),primary_key=True)


#########################################################################################################################################
class Budget(Base):
    __tablename__ = "budget"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)  # e.g., fuel, maintenance, insurance
    amount = Column(Float, nullable=False)
    date = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
    description = Column(String)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)

#########################################################################################################################################
class Fuel(Base):
    __tablename__ = "fuel"
    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    quantity = Column(Float, nullable=False)
    cost = Column(Float, nullable=False)
    date = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))

#########################################################################################################################################
class FuelLog(Base):
    __tablename__ = "fuel_logs"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    date = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
    fuel_type = Column(String, nullable=False)
    volume = Column(Float, nullable=False)  # in liters
    cost = Column(Float, nullable=False)

#########################################################################################################################################
class Maintenance(Base):
    __tablename__ = "maintenances"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    description = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    maintenance_date = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
#########################################################################################################################################
class Trip(Base):
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    departure_date =Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()')) 
    return_date = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    driver_id = Column(Integer, ForeignKey("users.id"))

#########################################################################################################################################

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer)
    plate_number = Column(String, unique=True, nullable=False)
    mileage = Column(Float, default=0.0)
    status = Column(String, default="available")  # available, in_use, maintenance