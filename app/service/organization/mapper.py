from typing import TYPE_CHECKING

from app.schema.organization import (
    ActivityResponse,
    BuildingResponse,
    OrganizationListResponse,
    OrganizationResponse,
    PhoneResponse,
)


if TYPE_CHECKING:
    from app.domain.activity import Activity
    from app.domain.building import Building
    from app.domain.organization import Organization
    from app.domain.phone import Phone


def map_building_to_dto(building: "Building") -> BuildingResponse:
    return BuildingResponse(
        id=building.id,
        address=building.address,
        latitude=building.latitude,
        longitude=building.longitude,
    )


def map_phone_to_dto(phone: "Phone") -> PhoneResponse:
    return PhoneResponse(
        id=phone.id,
        number=phone.number,
    )


def map_activity_to_dto(activity: "Activity") -> ActivityResponse:
    return ActivityResponse(
        id=activity.id,
        name=activity.name,
        level=activity.level,
    )


def map_organization_to_dto(organization: "Organization") -> OrganizationResponse:
    return OrganizationResponse(
        id=organization.id,
        name=organization.name,
        building=map_building_to_dto(building=organization.building),
        phone_numbers=[map_phone_to_dto(phone) for phone in organization.phones],
        activities=[map_activity_to_dto(activity) for activity in organization.activities],
    )


def map_organization_list_to_dto(organizations: list[Organization]) -> OrganizationListResponse:
    return OrganizationListResponse(
        items=[map_organization_to_dto(organization) for organization in organizations],
        total=len(organizations),
    )
