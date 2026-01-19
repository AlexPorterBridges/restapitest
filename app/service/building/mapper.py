from typing import TYPE_CHECKING

from app.schema.building import BuildingResponse


if TYPE_CHECKING:
    from app.domain.building import Building


def map_building_to_dto(building: "Building") -> BuildingResponse:
    return BuildingResponse(
        id=building.id,
        address=building.address,
        latitude=building.latitude,
        longitude=building.longitude,
    )
