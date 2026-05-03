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


@app.get("/cpu")
def cpu_load():
    total = 0

    for i in range(30_000_000):
        total += i * i

    return {
        "message": "cpu load completed",
        "result": total,
    }