import uuid

from sqlalchemy import Enum, ForeignKey, Text, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import TimestampMixin
from .enum import OrganizationStatus


class Organization(TimestampMixin):
    __tablename__ = "organizations"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(Text, nullable=False, index=True)

    building_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("buildings.id")
    )

    building = relationship(argument="Building", back_populates="organizations")

    phones = relationship(argument="Phone", cascade="all, delete-orphan")

    activities = relationship(
        argument="Activity",
        secondary="organization_activities",
        back_populates="organizations",
    )

    status: Mapped[OrganizationStatus] = mapped_column(
        Enum(OrganizationStatus, name="business_status"),
        nullable=False,
        default=OrganizationStatus.ACTIVE,
    )
