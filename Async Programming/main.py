import time
import asyncio
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return {
        "message":"async api"
    }

# def task():
#     time.sleep(3)
#     return "Done"


# async def task():
#     await asyncio.sleep(3)
#     return "Done"
