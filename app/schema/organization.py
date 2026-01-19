import uuid
from typing import Annotated

from pydantic import BaseModel, PositiveInt, StringConstraints

from app.schema.activity import ActivityResponse
from app.schema.base import BaseResponse
from app.schema.building import BuildingResponse


class PhoneResponse(BaseResponse):
    number: str


class OrganizationResponse(BaseResponse):
    id: uuid.UUID
    name: str
    building: BuildingResponse
    phone_numbers: list[PhoneResponse]
    activities: list[ActivityResponse]


class OrganizationListResponse(BaseModel):
    items: list[OrganizationResponse]
    total: int


class OrganizationSearchByNameRequest(BaseModel):
    name: str = Annotated[str, StringConstraints(min_length=1)]


class OrganizationByBuildingRequest(BaseModel):
    building_id: uuid.UUID


class OrganizationByActivityRequest(BaseModel):
    activity_id: uuid.UUID


class OrganizationRadiusRequest(BaseModel):
    latitude: float
    longitude: float
    radius: PositiveInt


class OrganizationCreateRequest(BaseModel):
    name: str
    building_id: uuid.UUID
    phone_numbers: list[str]
    activity_ids: list[uuid.UUID]


class OrganizationUpdateRequest(BaseModel):
    id: uuid.UUID
    name: str | None = None
    building_id: uuid.UUID | None = None
    phone_numbers: list[str] | None = None
    activity_ids: list[uuid.UUID] | None = None


class OrganizationDeleteRequest(BaseModel):
    id: uuid.UUID
