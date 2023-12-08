from __future__ import annotations
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Mesa(Base):
    __tablename__ = 'mesa'

    pedido_id: Mapped[int] = mapped_column(ForeignKey("pedidos.id"), primary_key=True)
    pedido = relationship("Pedido", back_populates="mesas")
    itemMenu = relationship("ItemMenu", back_populates="mesas")
