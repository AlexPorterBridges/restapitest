from .activity import router as activity_router
from .building import router as building_router
from .organization import router as organizations_router

__all__ = ["activity_router", "building_router", "organizations_router"]
