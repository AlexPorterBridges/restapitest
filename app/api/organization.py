import uuid

from fastapi import APIRouter, Depends, status

from app.factory.service import get_organization_service
from app.schema.organization import (
    OrganizationByActivityRequest,
    OrganizationByBuildingRequest,
    OrganizationCreateRequest,
    OrganizationDeleteRequest,
    OrganizationListResponse,
    OrganizationRadiusRequest,
    OrganizationResponse,
    OrganizationSearchByNameRequest,
    OrganizationUpdateRequest,
)
from app.service.organization import OrganizationService


router = APIRouter(
    prefix="/organization",
    tags=["Organization"],
)


@router.post(
    "/by-building/",
    response_model=OrganizationListResponse,
    summary="Список организаций в здании",
)
async def list_by_building(
    data: OrganizationByBuildingRequest,
    service: OrganizationService = Depends(get_organization_service),
) -> OrganizationListResponse:
    return await service.list_by_building(data)


@router.post(
    "/by-activity/",
    response_model=OrganizationListResponse,
    summary="Список организаций по виду деятельности",
)
async def list_by_activity(
    data: OrganizationByActivityRequest,
    service: OrganizationService = Depends(get_organization_service),
) -> OrganizationListResponse:
    return await service.list_by_activity(data)


@router.post(
    "/by-radius/",
    response_model=OrganizationListResponse,
    summary="Поиск организаций в радиусе от точки",
)
async def list_in_radius(
    data: OrganizationRadiusRequest,
    service: OrganizationService = Depends(get_organization_service),
) -> OrganizationListResponse:
    return await service.list_in_radius(data)


@router.post(
    "/by-activity-tree/",
    response_model=OrganizationListResponse,
    summary="Поиск организаций по виду деятельности, включая дочерние виды",
)
async def list_by_activity_tree(
    data: OrganizationByActivityRequest,
    service: OrganizationService = Depends(get_organization_service),
) -> OrganizationListResponse:
    return await service.list_by_activity_tree(data)


@router.post(
    "/search/",
    response_model=OrganizationListResponse,
    summary="Поиск организаций по названию",
)
async def search_by_name(
    data: OrganizationSearchByNameRequest,
    service: OrganizationService = Depends(get_organization_service),
) -> OrganizationListResponse:
    return await service.list_by_name(data)


@router.get(
    "/{id}",
    response_model=OrganizationResponse,
    summary="Получить организацию по ID",
)
async def get_organization(
    id: uuid.UUID,
    service: OrganizationService = Depends(get_organization_service),
) -> OrganizationResponse:
    return await service.get(id)


@router.post(
    "/create/",
    response_model=OrganizationResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Создать организацию",
)
async def create_organization(
    data: OrganizationCreateRequest,
    service: OrganizationService = Depends(get_organization_service),
) -> OrganizationResponse:
    return await service.create(data)


@router.post(
    "/update/",
    response_model=OrganizationResponse,
    summary="Редактировать организацию",
)
async def update_organization(
    data: OrganizationUpdateRequest,
    service: OrganizationService = Depends(get_organization_service),
) -> OrganizationResponse:
    return await service.update(data)


@router.post(
    "/delete/",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить организацию",
)
async def delete_organization(
    data: OrganizationDeleteRequest,
    service: OrganizationService = Depends(get_organization_service),
) -> None:
    await service.delete(data)
    return
