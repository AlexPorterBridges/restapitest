import uuid

from pydantic import BaseModel

from app.schema.base import BaseResponse


class BuildingResponse(BaseResponse):
    id: uuid.UUID
    address: str
    latitude: float
    longitude: float


class BuildingListResponse(BaseModel):
    items: list[BuildingResponse]
    total: int


class BuildingCreateRequest(BaseModel):
    address: str
    latitude: float
    longitude: float


class BuildingUpdateRequest(BaseModel):
    id: uuid.UUID
    address: str
    latitude: float
    longitude: float


class BuildingDeleteRequest(BaseModel):
    id: uuid.UUID
