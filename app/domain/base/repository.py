from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.base import TimestampMixin

if TYPE_CHECKING:
    pass


class BaseRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, entity: TimestampMixin) -> TimestampMixin:
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def update(self, entity: TimestampMixin) -> TimestampMixin:
        await self.session.commit()
        await self.session.refresh(entity)
        return entity
