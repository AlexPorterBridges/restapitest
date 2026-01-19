import uuid

from fastapi import APIRouter, Depends, status

from app.factory.service import get_activity_service
from app.schema.activity import (
    ActivityCreateRequest,
    ActivityDeleteRequest,
    ActivityResponse,
    ActivityUpdateRequest,
)
from app.service.activity import ActivityService


router = APIRouter(
    prefix="/activity",
    tags=["Activity"],
)


@router.get(
    "/{id}",
    response_model=ActivityResponse,
    summary="Получить организацию по ID",
)
async def get_activity(
    id: uuid.UUID,
    service: ActivityService = Depends(get_activity_service),
) -> ActivityResponse:
    return await service.get(id)


@router.post(
    "/create/",
    response_model=ActivityResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Создать деятельность",
)
async def create_activity(
    data: ActivityCreateRequest,
    service: ActivityService = Depends(get_activity_service),
) -> ActivityResponse:
    return await service.create(data)


@router.post(
    "/update/",
    response_model=ActivityResponse,
    summary="Редактировать деятельность",
)
async def update_activity(
    data: ActivityUpdateRequest,
    service: ActivityService = Depends(get_activity_service),
) -> ActivityResponse:
    return await service.update(data)


@router.post(
    "/delete/",
    response_model=ActivityResponse,
    summary="Удалить деятельность",
)
async def delete_activity(
    data: ActivityDeleteRequest,
    service: ActivityService = Depends(get_activity_service),
) -> None:
    await service.delete(data)
    return
