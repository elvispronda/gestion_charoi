#HERE WE USE FASTAPI WITH SQLALCHEMY :USING ORM

from fastapi import FastAPI

from . import models 
from .database import engine
from .routers import post, user, auth
from .config import settings

models.Base.metadata.create_all(bind = engine)

app = FastAPI(debug=True)        

    
  
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


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



































































































