import uuid

from pydantic import BaseModel

from app.schema.base import BaseResponse


class ActivityResponse(BaseResponse):
    id: uuid.UUID
    name: str
    level: int
    parent_id: uuid.UUID | None = None


class ActivityCreateRequest(BaseModel):
    name: str
    parent_id: uuid.UUID | None = None


class ActivityUpdateRequest(BaseModel):
    id: uuid.UUID
    name: str
    parent_id: uuid.UUID | None = None


class ActivityDeleteRequest(BaseModel):
    id: uuid.UUID
