from fastapi import FastAPI,status,HTTPException,Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app=FastAPI()



class UserNotFoundException(Exception):
    def __init__(self,name:str):
        self.name=name

@app.exception_handler(UserNotFoundException)
def user_not_found(request:Request,exc:UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"User {exc.name} not found"
        }
    )


# @app.get("/users/{user_id}")
# def get_user(user_id:int):
#     if user_id != 1:
#         raise HTTPException(
#             status_code=404,
#             detail="User Not Found"
#         )
#     return {
#         "id":1,
#         "name":"Anik"
#     }


@app.get("/users/{name}")
def get_user(name:str):
    if name!= 'Anik':
        raise UserNotFoundException (name)
    return {
        "name":name
    }