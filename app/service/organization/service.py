from typing import TYPE_CHECKING

from app.domain.activity import ActivityRepository
from app.domain.building import BuildingRepository
from app.domain.organization import Organization, OrganizationRepository, OrganizationStatus
from app.domain.phone import Phone
from app.factory.repository import (
    get_activity_repository,
    get_building_repository,
    get_organization_repository,
)
from app.service.organization.mapper import map_organization_list_to_dto, map_organization_to_dto
from app.utils.exception_handler import NotFoundError


if TYPE_CHECKING:
    import uuid
    from app.schema.organization import (
        OrganizationByActivityRequest,
        OrganizationByBuildingRequest,
        OrganizationDeleteRequest, OrganizationListResponse,
        OrganizationResponse,
        OrganizationSearchByNameRequest,
        OrganizationCreateRequest,
        OrganizationRadiusRequest,
        OrganizationUpdateRequest,
    )


class OrganizationService:
    def __init__(
        self,
        activity_repository: ActivityRepository = get_activity_repository(),
        building_repository: BuildingRepository = get_building_repository(),
        organization_repository: OrganizationRepository = get_organization_repository(),
    ):
        self.activity_repository = activity_repository
        self.building_repository = building_repository
        self.organization_repository = organization_repository

    async def get(self, id: "uuid.UUID") -> "OrganizationResponse":
        organization = await self.organization_repository.get(id)

        if not organization:
            raise NotFoundError("Organization")

        return map_organization_to_dto(organization=organization)

    async def list_by_name(self, data: "OrganizationSearchByNameRequest") -> "OrganizationListResponse":
        organizations = await self.organization_repository.list_by_name(data.name)

        if not organizations:
            raise NotFoundError("Organizations")

        return map_organization_list_to_dto(organizations=organizations)

    async def list_by_building(self, data: "OrganizationByBuildingRequest") -> "OrganizationListResponse":
        exists = await self.building_repository.get(data.building_id)
        if not exists:
            raise NotFoundError("Building")

        organizations = await self.organization_repository.list_by_building(building_id=data.building_id)

        if not organizations:
            raise NotFoundError("Organization")

        return map_organization_list_to_dto(organizations=organizations)

    async def list_by_activity(self, data: "OrganizationByActivityRequest") -> "OrganizationListResponse":
        exists = await self.activity_repository.get(data.activity_id)
        if not exists:
            raise NotFoundError("Activity")

        organizations = await self.organization_repository.list_by_activity(activity_id=data.activity_id)

        if not organizations:
            raise NotFoundError("Organization")

        return map_organization_list_to_dto(organizations=organizations)

    async def list_by_activity_tree(self, data: "OrganizationByActivityRequest") -> "OrganizationListResponse":
        exists = await self.activity_repository.get(data.activity_id)
        if not exists:
            raise NotFoundError("Activity")

        organizations = await self.organization_repository.list_by_activity_tree(activity_id=data.activity_id)

        if not organizations:
            raise NotFoundError("Organization")

        return map_organization_list_to_dto(organizations=organizations)

    async def list_in_radius(self, data: "OrganizationRadiusRequest") -> "OrganizationListResponse":
        organizations = await self.organization_repository.list_in_radius(
            latitude=data.latitude,
            longitude=data.longitude,
            radius=data.radius,
        )

        if not organizations:
            raise NotFoundError("Organization")

        return map_organization_list_to_dto(organizations=organizations)

    async def create(self, data: "OrganizationCreateRequest") -> "OrganizationResponse":
        building = await self.building_repository.get(data.building_id)
        if not building:
            raise NotFoundError("Building")

        activities = []
        for activity_id in data.activity_ids:
            exists = await self.activity_repository.get(activity_id)
            if not exists:
                raise NotFoundError("Activity")
            activities.append(exists)

        organization = Organization(
            name=data.name,
            building_id=data.building_id,
        )
        organization.phones = [Phone(number=p) for p in data.phone_numbers]
        organization.activities = activities

        _ = await self.organization_repository.create(organization)
        organization = await self.organization_repository.get(organization.id)
        return map_organization_to_dto(organization=organization)

    async def update(self, data: "OrganizationUpdateRequest") -> "OrganizationResponse":
        organization = await self.organization_repository.get(data.id)
        if not organization:
            raise NotFoundError("Organization")

        if data.name is not None:
            organization.name = data.name

        if data.building_id is not None:
            building = await self.building_repository.get(data.building_id)
            if not building:
                raise NotFoundError("Building")

        if data.phone_numbers is not None:
            organization.phones.clear()
            organization.phones.extend(
                Phone(number=number) for number in data.phone_numbers
            )

        if data.activity_ids is not None:
            activities = []
            for activity_id in data.activity_ids:
                exists = await self.activity_repository.get(activity_id)
                if not exists:
                    raise NotFoundError("Activity")

                activities.append(exists)
            organization.activities.clear()
            organization.activities.extend(activities)

        _ = await self.organization_repository.update(organization)
        organization = await self.organization_repository.get(organization.id)
        return map_organization_to_dto(organization=organization)

    async def delete(
        self,
        data: "OrganizationDeleteRequest",
    ) -> None:
        organization = await self.organization_repository.get(data.id)
        if not organization:
            raise NotFoundError("Organization")

        organization.status = OrganizationStatus.SUSPENDED

        _ = await self.organization_repository.update(organization)
