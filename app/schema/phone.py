import uuid

from app.schema.base import BaseResponse


class PhoneResponse(BaseResponse):
    id: uuid.UUID
    number: str
