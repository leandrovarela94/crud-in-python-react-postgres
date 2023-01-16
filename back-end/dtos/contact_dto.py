from pydantic import BaseModel, ValidationError, validator


class ContactDTO(BaseModel):
    id: int
    name: str
    phone: str
    email: str


@validator('name')
def name_validation(cls, name_insert):
    if len(name_insert) > 70:
        raise ValueError("name field contains too many characters")
    return name_insert


@validator('phone')
def name_validation(cls, phone_insert):
    if len(phone_insert) > 16:
        raise ValueError(" field contains too many characters")
    return phone_insert


@validator('email')
def name_validation(cls, email_insert):
    if len(email_insert) > 100:
        raise ValueError("name field contains too many characters")
    return email_insert
