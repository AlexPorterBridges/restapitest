from typing import TYPE_CHECKING

from app.domain.building import Building, BuildingRepository, BuildingStatus
from app.factory.repository import (get_building_repository)
from app.service.building.mapper import map_building_to_dto
from app.utils.exception_handler import AlreadyExistsError, NotFoundError


if TYPE_CHECKING:
    import uuid
    from app.schema.building import (
        BuildingCreateRequest,
        BuildingDeleteRequest,
        BuildingResponse, BuildingUpdateRequest,
    )


class BuildingService:
    def __init__(
        self,
        building_repository: BuildingRepository = get_building_repository(),
    ):
        self.building_repository = building_repository

    async def get(self, id: "uuid.UUID") -> "BuildingResponse":
        building = await self.building_repository.get(id)

        if not building:
            raise NotFoundError("Building")

        return map_building_to_dto(building=building)

    async def create(self, data: "BuildingCreateRequest") -> "BuildingResponse":
        exists = await self.building_repository.get_by_addtess(data.address)
        if exists:
            raise AlreadyExistsError("Building")

        building = Building(
            address=data.address,
            longitude=data.longitude,
            latitude=data.latitude,
        )

        _ = await self.building_repository.create(building)
        return map_building_to_dto(building=building)

    async def update(self, data: "BuildingUpdateRequest") -> "BuildingResponse":
        building = await self.building_repository.get(data.id)
        if not building:
            raise NotFoundError("Building")

        exists = await self.building_repository.get_by_addtess(data.address)
        if exists:
            raise AlreadyExistsError("Building")

        if data.address is not None:
            building.address = data.address

        if data.latitude is not None:
            building.latitude = data.latitude

        if data.longitude is not None:
            building.longitude = data.longitude

        _ = await self.building_repository.update(building)
        return map_building_to_dto(building=building)

    async def delete(
        self,
        data: "BuildingDeleteRequest",
    ) -> "BuildingResponse":
        building = await self.building_repository.get(data.id)
        if not building:
            raise NotFoundError("Building")

        building.status = BuildingStatus.SUSPENDED

        _ = self.building_repository.update(building)
        return map_building_to_dto(building=building)
