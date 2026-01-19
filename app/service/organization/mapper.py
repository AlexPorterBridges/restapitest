from typing import TYPE_CHECKING

from app.schema.organization import (
    OrganizationListResponse,
    OrganizationResponse,
    PhoneResponse,
)
from app.service.activity.mapper import map_activity_to_dto
from app.service.building.mapper import map_building_to_dto


if TYPE_CHECKING:
    from app.domain.organization import Organization
    from app.domain.phone import Phone


def map_phone_to_dto(phone: "Phone") -> PhoneResponse:
    return PhoneResponse(
        id=phone.id,
        number=phone.number,
    )


def map_organization_to_dto(organization: "Organization") -> OrganizationResponse:
    return OrganizationResponse(
        id=organization.id,
        name=organization.name,
        building=map_building_to_dto(building=organization.building),
        phone_numbers=[map_phone_to_dto(phone) for phone in organization.phones],
        activities=[map_activity_to_dto(activity) for activity in organization.activities],
    )


def map_organization_list_to_dto(organizations: "list[Organization]") -> OrganizationListResponse:
    return OrganizationListResponse(
        items=[map_organization_to_dto(organization) for organization in organizations],
        total=len(organizations),
    )
