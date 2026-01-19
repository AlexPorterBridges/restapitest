from typing import TYPE_CHECKING

from sqlalchemy import select

from app.domain.base import BaseRepository
from app.domain.building import Building


if TYPE_CHECKING:
    import uuid


class BuildingRepository(BaseRepository):
    async def get(self, id: "uuid.UUID") -> Building | None:
        result = await self.session.execute(
            select(Building).where(Building.id == id)
        )
        return result.scalar_one_or_none()
