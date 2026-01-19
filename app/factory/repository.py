from functools import lru_cache

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.domain.activity.repository import ActivityRepository
from app.domain.building.repository import BuildingRepository
from app.domain.organization import OrganizationRepository


@lru_cache
def get_organization_repository(
    session: AsyncSession = Depends(get_db),
) -> OrganizationRepository:
    return OrganizationRepository(session=session)


@lru_cache
def get_building_repository(
    session: AsyncSession = Depends(get_db),
) -> BuildingRepository:
    return BuildingRepository(session=session)


@lru_cache
def get_activity_repository(
    session: AsyncSession = Depends(get_db),
) -> ActivityRepository:
    return ActivityRepository(session=session)
