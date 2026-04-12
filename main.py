from fastapi import FastAPI
import time

app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "hello"}


@app.get("/slow")
def slow():
    time.sleep(2)
    return {"message": "slow"}