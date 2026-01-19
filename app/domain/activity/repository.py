from typing import TYPE_CHECKING

from sqlalchemy import select

from app.domain.activity import Activity
from app.domain.base import BaseRepository

if TYPE_CHECKING:
    import uuid


class ActivityRepository(BaseRepository):
    async def get(self, id: "uuid.UUID") -> Activity | None:
        result = await self.session.execute(select(Activity).where(Activity.id == id))
        return result.scalar_one_or_none()

    async def list_all(self) -> list[Activity]:
        result = await self.session.execute(select(Activity))
        return list(result.scalars().all())
