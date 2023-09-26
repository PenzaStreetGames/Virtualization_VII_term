import logging
from typing import Union, Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import json
from random import randint
import os
from fastapi.responses import FileResponse

from second_part.db import PostgresDatabaseAdapter

app = FastAPI()


databaseAdapter = PostgresDatabaseAdapter()


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


@app.get("/")
def read_root():
    return {"Hello": "Tyler"}


@app.get("/items/")
def read_items():
    return databaseAdapter.find_all("items")


@app.post("/items/", response_model=Item)
def create_item(item: Item):
    databaseAdapter.create("items", [item.id, item.name, item.description])
    return item


# Пример эндпоинта для получения фото герба
@app.get("/gerb")
async def get_gerb():
    return FileResponse("mirea_gerb.png")


if __name__ == "__main__":
    #uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('APP_PORT')))
    uvicorn.run(app, host="0.0.0.0", port=8012)
