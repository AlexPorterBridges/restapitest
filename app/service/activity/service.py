from typing import TYPE_CHECKING

from app.domain.activity import Activity, ActivityRepository, ActivityStatus
from app.factory.repository import (get_activity_repository)
from app.service.activity.mapper import map_activity_to_dto
from app.utils.exception_handler import NotFoundError


if TYPE_CHECKING:
    import uuid
    from app.schema.activity import (
        ActivityCreateRequest,
        ActivityDeleteRequest,
        ActivityResponse, ActivityUpdateRequest,
    )


class ActivityService:
    def __init__(
        self,
        activity_repository: ActivityRepository = get_activity_repository(),
    ):
        self.activity_repository = activity_repository

    async def get(self, id: "uuid.UUID") -> "ActivityResponse":
        activity = await self.activity_repository.get(id)

        if not activity:
            raise NotFoundError("Activity")

        return map_activity_to_dto(activity=activity)

    async def create(self, data: "ActivityCreateRequest") -> "ActivityResponse":
        building = await self.activity_repository.get(data.parent_id)
        if not building:
            raise NotFoundError("Activity")

        activity = Activity(
            name=data.name,
            parent_id=data.parent_id,
            level=data.level,
        )

        _ = await self.activity_repository.create(activity)
        return map_activity_to_dto(activity=activity)

    async def update(self, data: "ActivityUpdateRequest") -> "ActivityResponse":
        activity = await self.activity_repository.get(data.id)
        if not activity:
            raise NotFoundError("Activity")

        if data.name is not None:
            activity.name = data.name

        if data.level is not None:
            activity.level = data.level

        if data.paren_id is not None:
            parent = await self.activity_repository.get(data.parent_id)
            if not parent:
                raise NotFoundError("Activity")

            activity.parent_id = data.parent_id

        _ = await self.activity_repository.update(activity)
        return map_activity_to_dto(activity=activity)

    async def delete(
        self,
        data: "ActivityDeleteRequest",
    ) -> "ActivityResponse":
        activity = await self.activity_repository.get(data.id)
        if not activity:
            raise NotFoundError("Activity")

        activity.status = ActivityStatus.SUSPENDED

        _ = self.activity_repository.update(activity)
        return map_activity_to_dto(activity=activity)
