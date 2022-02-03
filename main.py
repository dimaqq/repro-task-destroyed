import asyncio

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def foobar():
    await asyncio.sleep(9)
    return {"foo": "bar"}
