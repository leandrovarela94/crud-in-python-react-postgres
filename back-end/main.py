from typing import Union

from dtos import contact_dto
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root(contact_dto):
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
