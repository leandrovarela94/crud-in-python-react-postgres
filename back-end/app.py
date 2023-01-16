from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Contact(BaseModel):
    id: Optional[int]
    name: str
    phone: str
    email: str


@app.get("/contacts")
def read_root(name):
    response = name

    return {f"Sucess : response: {response}"}
