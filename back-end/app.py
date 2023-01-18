from fastapi import FastAPI, Query
from pydantic import BaseModel
from sql.postgres import Postgres

app = FastAPI()


@app.get("/contacts/")
async def read_all():
    query = 'SELECT * FROM list_contacts'
    result = Postgres.get_contacts_postgres(query)

    return result


@app.get("/contacts/{id}")
async def read_one(id: int):
    query = f"SELECT * FROM list_contacts WHERE id ={id}"
    result = Postgres.get_contacts_postgres(query)

    return result


@app.post("/contacts/")
async def create_contact(name: str, phone: str, email: str):
    query = f"INSERT INTO list_contacts (name,phone,email) VALUES('{name}','{phone}','{email}')"
    Postgres.post_contacts_postgres(query)
    print(query)
    return {f"Sucess : response:"}


@app.delete("/contacts/{id}")
async def delete_contact(id: int):
    id_query: str = id
    query = f"DELETE FROM list_contacts WHERE id = {id_query} ;"
    Postgres.post_delete_postgres(query)
    print(query)
    return {f"Sucess : response:"}


@app.put("/contacts/{id}")
async def update_contact(name: str, phone: str, email: str, id: int):
    query = f"UPDATE list_contacts set name = '{name}', phone = '{phone}', email = '{email}' WHERE id = ({id}) ;"
    Postgres.post_update_postgres(query)
    print(query)
    return {f"Sucess : response:"}
