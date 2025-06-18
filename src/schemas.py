from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import date
from typing import Optional


class ContactModel(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    birth_date: date
    description: Optional[str] = None


class ContactResponse(ContactModel):
    id: int

    model_config = ConfigDict(from_attributes=True)
