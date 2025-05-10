# main.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

app = FastAPI()

# Allow CORS for local development (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy user for example
fake_user = {
    "username": "root",
    "password": "pswd",  # Never store plain passwords in production!
    "token": "sample.jwt.token"
}

class LoginData(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(data: LoginData):
    if data.username == fake_user["username"] and data.password == fake_user["password"]:
        return {"access_token": fake_user["token"], "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid username or password")
