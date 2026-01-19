from functools import lru_cache

from fastapi import Depends

from app.domain.activity import ActivityRepository
from app.domain.building import BuildingRepository
from app.domain.organization import OrganizationRepository
from app.service.organization import OrganizationService
from .repository import (
    get_activity_repository,
    get_building_repository,
    get_organization_repository,
)
from ..service.activity import ActivityService
from ..service.building import BuildingService


@lru_cache
def get_organization_service(
    activity_repository: ActivityRepository = Depends(get_activity_repository),
    building_repository: BuildingRepository = Depends(get_building_repository),
    organization_repository: OrganizationRepository = Depends(get_organization_repository),
) -> OrganizationService:
    return OrganizationService(
        activity_repository=activity_repository,
        building_repository=building_repository,
        organization_repository=organization_repository,
    )


@lru_cache
def get_activity_service(
    activity_repository: ActivityRepository = Depends(get_activity_repository),
) -> ActivityService:
    return ActivityService(
        activity_repository=activity_repository,
    )


@lru_cache
def get_building_service(
    building_repository: BuildingRepository = Depends(get_building_repository),
) -> BuildingService:
    return BuildingService(
        building_repository=building_repository,
    )
