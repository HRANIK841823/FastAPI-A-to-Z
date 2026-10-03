from fastapi import FastAPI

app = FastAPI()

#Home Route
@app.get("/")
def home():
    return {"message": "FastAPI is running"}

#About Route
@app.get("/about")
def about():
    return{"Message":"This is About Page"}


#User Route
@app.get("/users")
def about():
    return{
        "users":["Akram","Karim","Meherab"]
    }
