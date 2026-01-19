from typing import TYPE_CHECKING

from app.schema.building import BuildingListResponse, BuildingResponse

if TYPE_CHECKING:
    from app.domain.building import Building


def map_building_to_dto(building: "Building") -> BuildingResponse:
    return BuildingResponse(
        id=building.id,
        address=building.address,
        latitude=building.latitude,
        longitude=building.longitude,
    )


def map_building_list_to_dto(buildings: "list[Building]") -> BuildingListResponse:
    return BuildingListResponse(
        items=[map_building_to_dto(building) for building in buildings],
        total=len(buildings),
    )
