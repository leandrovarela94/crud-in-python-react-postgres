from fastapi import FastAPI, Query
from models.contact import Contact
from services.contact_services import ContactSevices

app = FastAPI()


@app.get("/contacts/")
async def read_all():
    result = ContactSevices.get_contact_postgres()

    return result


@app.get("/contacts/{id}")
async def read_one(id: int):

    result = ContactSevices.get_one_contacts_postgres(id)

    return result


@app.post("/contacts/")
def create_contact(contact: Contact):

    ContactSevices.post_contacts_postgres(contact)

    return {f"Sucess Created"}


@app.delete("/contacts/{id}")
def delete_contact(id: int):

    x = ContactSevices.delete_contact_postgres(id)
    return {f"Sucess : Deleted"}


@app.put("/contacts/{id}")
def update_contact(contact: Contact, id: int):

    x = ContactSevices.update_contact_postgres(
        contact, id)

    return {f"Sucess Updated"}
