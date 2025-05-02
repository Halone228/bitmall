from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime
from functools import partial
from pytz import utc


class CRUDTimeMixin:
    created_at: Mapped[datetime] = mapped_column(
        default_factory=partial(datetime.now, tz=utc)
    )
    updated_at: Mapped[datetime | None] = mapped_column(
        default=None,
        onupdate=partial(datetime.now, tz=utc)
    )
    deleted_at: Mapped[datetime | None] = mapped_column(
        default=None
    )

