from typing import TYPE_CHECKING

from sqlalchemy import select

from app.domain.base import BaseRepository
from app.domain.phone import Phone


if TYPE_CHECKING:
    import uuid


class PhoneRepository(BaseRepository):
    async def get(self, id: "uuid.UUID") -> Phone | None:
        result = await self.session.execute(
            select(Phone).where(Phone.id == id)
        )
        return result.scalar_one_or_none()
