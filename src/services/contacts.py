from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.contacts import ContactsRepository
from src.schemas import ContactModel


class ContactsService:
    def __init__(self, db: AsyncSession):
        self.repository = ContactsRepository(db)

    async def create_contact(self, body: ContactModel):
        return await self.repository.create_contact(body)

    async def get_contacts(self, skip: int, limit: int):
        return await self.repository.get_contacts(skip, limit)

    async def get_contact(self, contact_id: int):
        return await self.repository.get_contact_by_id(contact_id)

    async def search_contacts(self, query: str):
        return await self.repository.search_contacts(query)

    async def get_birthdays_next_week(self):
        return await self.repository.get_birthdays_next_week()

    async def update_contact(self, contact_id: int, body: ContactModel):
        return await self.repository.update_contact(contact_id, body)

    async def remove_contact(self, contact_id: int):
        return await self.repository.remove_contact(contact_id)
