from typing import TYPE_CHECKING

from sqlalchemy import and_, func, select
from sqlalchemy.orm import aliased, selectinload

from app.domain.activity import Activity, OrganizationActivity
from app.domain.base import BaseRepository
from app.domain.building import Building
from app.domain.organization import Organization, OrganizationStatus


if TYPE_CHECKING:
    import uuid


class OrganizationRepository(BaseRepository):
    async def get(self, id: "uuid.UUID") -> Organization | None:
        result = await self.session.execute(
            select(Organization).where(
                and_(
                    Organization.id == id,
                    Organization.status != OrganizationStatus.SUSPENDED
                ),
            ).options(
                selectinload(Organization.phones),
                selectinload(Organization.activities),
                selectinload(Organization.building),
            )
        )
        return result.scalar_one_or_none()

    async def list_by_name(self, name: str) -> list[Organization]:
        stmt = (
            select(Organization)
            .where(Organization.name.ilike(f"%{name}%"))
            .options(
                selectinload(Organization.building),
                selectinload(Organization.phones),
                selectinload(Organization.activities),
            )
        )

        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def list_by_building(self, building_id: "uuid.UUID") -> list[Organization]:
        query = (
            select(Organization)
            .where(
                and_(
                    Organization.building_id == building_id,
                    Organization.status != OrganizationStatus.SUSPENDED
                ),
            ).options(
                selectinload(Organization.phones),
                selectinload(Organization.activities)
            )
        )

        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def list_by_activity(self, activity_id: "uuid.UUID") -> list[Organization]:
        query = (
            select(Organization)
            .join(OrganizationActivity)
            .where(
                and_(
                    OrganizationActivity.activity_id == activity_id,
                    Organization.status != OrganizationStatus.SUSPENDED
                ),
            )
            .options(
                selectinload(Organization.phones),
                selectinload(Organization.building),
                selectinload(Organization.activities),
            )
        )

        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def list_in_radius(self, latitude: float, longitude: float, radius: float) -> list[Organization]:
        earth_radius = 6371000

        lat1 = func.radians(latitude)
        lon1 = func.radians(longitude)
        lat2 = func.radians(Building.latitude)
        lon2 = func.radians(Building.longitude)

        distance = earth_radius * func.acos(
            func.cos(lat1)
            * func.cos(lat2)
            * func.cos(lon2 - lon1)
            + func.sin(lat1) * func.sin(lat2)
        )

        stmt = (
            select(Organization)
            .join(Organization.building)
            .where(
                and_(
                    distance <= radius,
                    Organization.status != OrganizationStatus.SUSPENDED
                ),
            )
            .options(
                selectinload(Organization.building),
                selectinload(Organization.phones),
                selectinload(Organization.activities),
            )
        )

        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def _get_activity_subtree_ids(self, root_activity_id: "uuid.UUID") -> list["uuid.UUID"]:
        activity_alias = aliased(Activity)

        cte = (
            select(Activity.id)
            .where(Activity.id == root_activity_id)
            .cte(name="activity_cte", recursive=True)
        )

        cte = cte.union_all(
            select(activity_alias.id)
            .where(activity_alias.parent_id == cte.c.id)
        )

        result = await self.session.execute(select(cte.c.id))
        return list(result.scalars().all())

    async def list_by_activity_tree(self, activity_id: "uuid.UUID") -> list[Organization]:
        activity_ids = await self._get_activity_subtree_ids(activity_id)

        stmt = (
            select(Organization)
            .join(OrganizationActivity)
            .where(
                and_(
                    OrganizationActivity.activity_id.in_(activity_ids),
                    Organization.status != OrganizationStatus.SUSPENDED
                ),
            )
            .distinct()
            .options(
                selectinload(Organization.activities),
                selectinload(Organization.building),
                selectinload(Organization.phones),
            )
        )

        result = await self.session.execute(stmt)
        return list(result.scalars().all())
