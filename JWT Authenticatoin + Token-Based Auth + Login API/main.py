from fastapi import FastAPI,Depends,HTTPException,Header
from jose import jwt
from datetime import datetime,timedelta,timezone


app=FastAPI()


SECRET_KEY="mysecret"

ALGORITHM="HS256"

#Create token
def create_token(data:dict):
    to_endcode=data.copy()
    expire=datetime.now(timezone.utc) + timedelta(minutes=30)
    to_endcode.update({
        "exp":expire
    })
    token=jwt.encode(to_endcode,SECRET_KEY,algorithm=ALGORITHM)

    return token

#login Api (Token Generation)
@app.post("/login")
def login(username:str,password:str):
    if username != "admin" or password != "1234":
        raise HTTPException (status_code=401,detail="Invalid Username & Password")
    token = create_token({
        "sub":username
    })
    return {
        "access_token":token
    }

#Token Verification
def token_verify(token:str=Header(None)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        return payload

    except:
        raise HTTPException(status_code=401,detail="Invalid or expired token")

#Protected Route
@app.get("/secure")
def secured_data(user=Depends(token_verify)):
    return {
        "message":"Secure Data Accessed",
        "user":user
    }