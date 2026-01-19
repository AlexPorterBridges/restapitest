from fastapi import Depends

from app.domain.activity import ActivityRepository
from app.domain.building import BuildingRepository
from app.domain.organization import OrganizationRepository
from app.domain.phone import PhoneRepository
from app.service.organization import OrganizationService
from .repository import (
    get_activity_repository,
    get_building_repository,
    get_organization_repository,
    get_phone_repository,
)


def get_organization_service(
    activity_repository: ActivityRepository = Depends(get_activity_repository),
    building_repository: BuildingRepository = Depends(get_building_repository),
    organization_repository: OrganizationRepository = Depends(get_organization_repository),
    phone_repository: PhoneRepository = Depends(get_phone_repository),
) -> OrganizationService:
    return OrganizationService(
        activity_repository=activity_repository,
        building_repository=building_repository,
        organization_repository=organization_repository,
        phone_repository=phone_repository,
    )
