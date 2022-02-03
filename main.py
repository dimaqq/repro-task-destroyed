import asyncio

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def foobar():
    await asyncio.sleep(99)
    return {"foo": "bar"}
