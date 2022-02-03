from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def foobar():
    return {"foo": "bar"}
