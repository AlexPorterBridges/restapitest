import uuid

from sqlalchemy import ForeignKey, Text, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import TimestampMixin


class Phone(TimestampMixin):
    __tablename__ = "phones"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    organization_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("organization.id")
    )

    number: Mapped[str] = mapped_column(Text, nullable=False)
