from fastapi import FastAPI

app=FastAPI()


@app.post("/create_user")
def create_user(user:dict):
    return{
        "Message":"User Created Successfully",
        "data":user
    }