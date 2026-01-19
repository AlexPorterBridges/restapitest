from typing import TYPE_CHECKING

from app.domain.activity import Activity, ActivityRepository, ActivityStatus
from app.factory.repository import (get_activity_repository)
from app.schema.activity import ActivityListResponse
from app.service.activity.mapper import map_activity_list_to_dto, map_activity_to_dto
from app.utils.exception_handler import NotFoundError, UnprocessableEntityError


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
        activity = Activity(
            name=data.name,
        )

        if data.parent_id:
            parent = await self.activity_repository.get(data.parent_id)
            if not parent:
                raise NotFoundError("Parent activity")

            activity.parent_id = data.parent_id
            activity.parent = parent
            activity.level = parent.level + 1
            if activity.level > 3:
                msg = "Inheritance from this parent is not possible, inheritance level exceeded"
                raise UnprocessableEntityError(msg)

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

        if data.parent_id is not None:
            parent = await self.activity_repository.get(data.parent_id)
            if not parent:
                raise NotFoundError("Parent activity")

            activity.parent_id = data.parent_id

        _ = await self.activity_repository.update(activity)
        return map_activity_to_dto(activity=activity)

    async def delete(
        self,
        data: "ActivityDeleteRequest",
    ) -> None:
        activity = await self.activity_repository.get(data.id)
        if not activity:
            raise NotFoundError("Activity")

        activity.status = ActivityStatus.SUSPENDED

        _ = self.activity_repository.update(activity)

    async def list_all(self) -> "ActivityListResponse":
        activities = await self.activity_repository.list_all()

        if not activities:
            raise NotFoundError("Activities")

        return map_activity_list_to_dto(activities=activities)
