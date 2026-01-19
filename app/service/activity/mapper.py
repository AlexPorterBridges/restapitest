from typing import TYPE_CHECKING

from app.schema.organization import (
    ActivityResponse,
)


if TYPE_CHECKING:
    from app.domain.activity import Activity


def map_activity_to_dto(activity: "Activity") -> ActivityResponse:
    return ActivityResponse(
        id=activity.id,
        name=activity.name,
        level=activity.level,
    )
