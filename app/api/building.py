import uuid

from fastapi import APIRouter, Depends, status

from app.factory.service import get_building_service
from app.schema.building import (
    BuildingCreateRequest,
    BuildingDeleteRequest,
    BuildingListResponse, BuildingResponse,
    BuildingUpdateRequest,
)
from app.service.building import BuildingService


router = APIRouter(
    prefix="/building",
    tags=["Building"],
)


@router.get(
    "/{id}",
    response_model=BuildingResponse,
    summary="Получить организацию по ID",
)
async def get_building(
    id: uuid.UUID,
    service: BuildingService = Depends(get_building_service),
) -> BuildingResponse:
    return await service.get(id)


@router.post(
    "/create/",
    response_model=BuildingResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Создать здание",
)
async def create_building(
    data: BuildingCreateRequest,
    service: BuildingService = Depends(get_building_service),
) -> BuildingResponse:
    return await service.create(data)


@router.post(
    "/update/",
    response_model=BuildingResponse,
    summary="Редактировать здание",
)
async def update_building(
    data: BuildingUpdateRequest,
    service: BuildingService = Depends(get_building_service),
) -> BuildingResponse:
    return await service.update(data)


@router.post(
    "/delete/",
    response_model=BuildingResponse,
    summary="Удалить здание",
)
async def delete_building(
    data: BuildingDeleteRequest,
    service: BuildingService = Depends(get_building_service),
) -> None:
    await service.delete(data)
    return


@router.get(
    "/",
    response_model=BuildingListResponse,
    summary="Получить все здания",
)
async def list_all(
    service: BuildingService = Depends(get_building_service),
) -> BuildingListResponse:
    return await service.list_all()
