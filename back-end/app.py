from typing import Optional

from adapters.postgres import Postgres
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/contacts")
def read_root():
    query = 'SELECT * FROM list_contacts'
    result = Postgres.get_contacts_postgres(query)

    return result


@app.post("/contacts")
def create_contatct(name: str, phone: str, email: str):
    query = f"INSERT INTO list_contacts (name,phone,email) VALUES('{name}','{phone}','{email}');"
    Postgres.post_contacts_postgres(query)
    print(query)
    return {f"Sucess : response:"}
