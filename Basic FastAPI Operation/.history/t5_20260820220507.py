from fastapi import FastAPI

app=FastAPI()


#Users Route
@app.get("/users")
def get_users(name):
    return{"Name":name}
