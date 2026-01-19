from typing import TYPE_CHECKING

from app.schema.activity import ActivityListResponse, ActivityResponse

if TYPE_CHECKING:
    from app.domain.activity import Activity


def map_activity_to_dto(activity: "Activity") -> ActivityResponse:
    return ActivityResponse(
        id=activity.id,
        name=activity.name,
        level=activity.level,
        parent_id=activity.parent_id,
    )


def map_activity_list_to_dto(activities: "list[Activity]") -> ActivityListResponse:
    return ActivityListResponse(
        items=[map_activity_to_dto(activity) for activity in activities],
        total=len(activities),
    )
