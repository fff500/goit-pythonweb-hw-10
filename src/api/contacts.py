from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.schemas import ContactResponse, ContactModel
from src.services.contacts import ContactsService

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/", response_model=List[ContactResponse])
async def read_contacts(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    contacts_service = ContactsService(db)
    contacts = await contacts_service.get_contacts(skip, limit)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse)
async def read_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contacts_service = ContactsService(db)
    contact = await contacts_service.get_contact(contact_id)
    print(contact)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.get("/search/")
async def search_contacts(query: str, db: AsyncSession = Depends(get_db)):
    contacts_service = ContactsService(db)
    contacts = await contacts_service.search_contacts(query)
    print(contacts)
    if not contacts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contacts not found"
        )
    return contacts


@router.get("/birthdays/", response_model=List[ContactResponse])
async def get_birthdays_next_week(db: AsyncSession = Depends(get_db)):
    contacts_service = ContactsService(db)
    contacts = await contacts_service.get_birthdays_next_week()
    print(contacts)
    if not contacts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contacts not found"
        )
    return contacts


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactModel, db: AsyncSession = Depends(get_db)):
    contacts_service = ContactsService(db)
    return await contacts_service.create_contact(body)


@router.patch("/{contact_id}", response_model=ContactResponse)
async def update_contact(
    body: ContactModel, contact_id: int, db: AsyncSession = Depends(get_db)
):
    contacts_service = ContactsService(db)
    contact = await contacts_service.update_contact(contact_id, body)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.delete("/{contact_id}", response_model=ContactResponse)
async def remove_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contacts_service = ContactsService(db)
    contact = await contacts_service.remove_contact(contact_id)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact
