from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# import os
# from dotenv import load_dotenv

# load_dotenv()

 
from config import settings
origins=settings.origins
SECRET_KEY=settings.SECRET_KEY
DB_URL=settings.DB_URL




# React এবং FastAPI-এর মধ্যে CORS permission দেওয়া
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Simple API endpoint
@app.get("/")
def home():
    return {
        "message": "CORS Enabled Hello World"
    }