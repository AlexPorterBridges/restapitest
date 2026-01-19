import uuid

from pydantic import BaseModel


class BaseResponse(BaseModel):
    id: uuid.UUID

    model_config = {
        "from_attributes": True
    }
