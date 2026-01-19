from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.domain.activity.repository import ActivityRepository
from app.domain.building.repository import BuildingRepository
from app.domain.organization import OrganizationRepository
from app.domain.phone import PhoneRepository


def get_organization_repository(
    session: AsyncSession = Depends(get_db),
) -> OrganizationRepository:
    return OrganizationRepository(session=session)


def get_building_repository(
    session: AsyncSession = Depends(get_db),
) -> BuildingRepository:
    return BuildingRepository(session=session)


def get_activity_repository(
    session: AsyncSession = Depends(get_db),
) -> ActivityRepository:
    return ActivityRepository(session=session)


def get_phone_repository(
    session: AsyncSession = Depends(get_db),
) -> PhoneRepository:
    return PhoneRepository(session=session)
