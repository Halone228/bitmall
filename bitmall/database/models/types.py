from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from typing import TypeAlias

s3_id_column = mapped_column(
   String(length=255) 
)
s3_id_type: TypeAlias = Mapped[str]
