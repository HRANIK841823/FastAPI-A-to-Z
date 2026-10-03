from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# React frontend-এর URL
origins = [
    "http://localhost:5173"
]


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