from typing import Union

from fastapi import FastAPI
import datetime

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/time")
def time():
    return {"Time": str(datetime.datetime.now().strftime('%H:%M'))}

@app.get("/date")
def date():
    return {"Date": str(datetime.datetime.now().strftime('%Y:%m:%d'))}
