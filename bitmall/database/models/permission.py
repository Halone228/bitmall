from sqlalchemy import String, ForeignKey, Enum, BIGINT
from sqlalchemy.orm import mapped_column, Mapped
from .base import Base
from .enums import RolesEnum
from .mixins import CRUDTimeMixin


class Role(CRUDTimeMixin, Base):
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'), primary_key=True
    )
    role: Mapped[RolesEnum] = mapped_column(
        Enum(RolesEnum), default=RolesEnum.user
    )


class Permission(CRUDTimeMixin, Base):
    id: Mapped[int] = mapped_column(
        BIGINT(), primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id')
    )
    permission: Mapped[str] = mapped_column(
        String(length=320), unique=True
    )


__all__ = [
    'Role',
    'Permission'
]
