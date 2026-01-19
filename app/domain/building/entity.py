import uuid

from sqlalchemy import Numeric, Text, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import TimestampMixin


class Building(TimestampMixin):
    __tablename__ = "buildings"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    address: Mapped[str] = mapped_column(Text, nullable=False)

    latitude: Mapped[float] = mapped_column(
        Numeric(9, 6),
        nullable=False,
    )

    longitude: Mapped[float] = mapped_column(
        Numeric(9, 6),
        nullable=False,
    )

    organizations = relationship("Organization", back_populates="buildings")
