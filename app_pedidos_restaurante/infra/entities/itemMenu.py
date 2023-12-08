from __future__ import annotations
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class ItemMenu(Base):
    __tablename__ = 'itemMenu'

