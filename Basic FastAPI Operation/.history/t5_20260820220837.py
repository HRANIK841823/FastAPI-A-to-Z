from fastapi import FastAPI

app=FastAPI()


#Users Route
@app.get("/users")
def get_users(name:str=None):
    return{"Name":name}



#Products Route
@app.get("/products")
def get_products(limit: int=20):
    return{"Limit" : limit}
