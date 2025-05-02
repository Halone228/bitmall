from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, BIGINT, ForeignKey, select, SQLColumnExpression, and_
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from .base import Base
from .mixins import CRUDTimeMixin
from .types import s3_id_column, s3_id_type
from .permission import Permission, Role


class UserModel(SQLAlchemyBaseUserTable[int], CRUDTimeMixin, Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column( # type: ignore
        BIGINT(), primary_key=True
    )
    icon_id: s3_id_type = s3_id_column
    username: Mapped[str] = mapped_column(
        String(length=255)
    )
    first_name: Mapped[str] = mapped_column(
        String(length=63), nullable=True
    )
    last_name: Mapped[str] = mapped_column(
        String(length=63), nullable=True
    )
    user_settings: Mapped["UserSettings"]
    _role: Mapped[Role] = relationship()
    _permissions: Mapped[list[Permission]] = relationship()

    @hybrid_method
    def has_permission(self, permission: str):
        return permission in [i.permission for i in self._permissions]

    @hybrid_property
    def permissions(self):
        return tuple(i.permission for i in self._permissions)

    @permissions.expression
    @classmethod
    def _permissions_expression(cls) -> SQLColumnExpression[tuple[str]]:
        return select(Permission.permission).where(
            Permission.user_id == cls.id
        ).label("permissions")

    @has_permission.expression
    @classmethod
    def _has_permission_expression(cls, permission: str) -> SQLColumnExpression[bool]:
        return select(
            Permission.permision
        ).where(and_(Permission.user_id==cls.id, Permission.permission == permission)).exists()

    @property
    def role(self):
        return self._role.role.name

    



class UserSettings(CRUDTimeMixin, Base):
    __tablename__ = 'user_settings'
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'), primary_key=True
    )
    dark_theme: Mapped[bool] = mapped_column(
        default=False
    )




