#HERE WE USE FASTAPI WITH SQLALCHEMY :USING ORM

from fastapi import FastAPI
from . import models 
from .database import engine
from .routers import  user, auth,category_document,vehicle_make,vehicle_model,vehicle_type,vehicle_transmission,category_maintenance,category_panne,document_vehicle,driver,vehicle,fuel,garage,panne,reparation,trip,fuel_type
from .config import settings
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

models.Base.metadata.create_all(bind = engine)

app = FastAPI(debug=True) 


""" # CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files at a non-root path
app.mount("/static", StaticFiles(directory="frontend", html=True), name="static") """

# Include your routers
app.include_router(auth.router)  
app.include_router(user.router)
app.include_router(category_document.router)
app.include_router(category_maintenance.router)
app.include_router(category_panne.router)
app.include_router(document_vehicle.router)
app.include_router(driver.router)
app.include_router(fuel.router)
app.include_router(garage.router)
app.include_router(panne.router)
app.include_router(reparation.router)
app.include_router(trip.router)
app.include_router(fuel_type.router)
app.include_router(vehicle.router)
app.include_router(vehicle_make.router)
app.include_router(vehicle_model.router)
app.include_router(vehicle_transmission.router)
app.include_router(vehicle_type.router)


#show all cars that have been in pannes for more than 10 days
#CV for each car:
           #Number of Maintenance                  -Howmuch it cost                              -details
           #volume of oil(fuel)                    -Howmuch it cost                              -details
           #Number of pannes                       -Howmuch it cost                              -details
           #Number of reparation                   -Howmuch it cost                              -details
           #Number of spare parts                  -Howmuch it cost                              -details

# compare using different charts
#Compare car cost vs all services done if is greater than 1/2 .consider to sell it

#List of comming trip :status(count how many left days), Trip history + details
# Warning for document soon to be expire
#split car into 3 categories:(Available, Inuse, In Dommage, Booked) : List and full details.



# Expenditure guidlines:
                    #Fuel              #Spare parts       #Reparation      #Maintenance



#check now if it works perfectly



































































































                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        