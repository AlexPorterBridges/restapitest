import uuid
from typing import Annotated

from pydantic import BaseModel, PositiveInt, StringConstraints

from app.schema.base import BaseResponse


class PhoneResponse(BaseResponse):
    id: uuid.UUID
    number: str
