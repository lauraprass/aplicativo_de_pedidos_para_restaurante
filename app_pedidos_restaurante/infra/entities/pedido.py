from __future__ import annotations
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Pedido(Base):
    __tablename__ = 'pedido'

    mesa_id: Mapped[int] = mapped_column(ForeignKey("mesas.id"), primary_key=True)
    