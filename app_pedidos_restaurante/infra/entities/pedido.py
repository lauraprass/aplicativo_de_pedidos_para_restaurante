from __future__ import annotations
from typing import List
from sqlalchemy import Column, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.config.base import Base


class Pedido(Base):
    __tablename__ = 'pedido'

    id = Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    num_pedido = Mapped[int] = mapped_column(nullable=False)
    itens_pedido = relationship("ItemMenuPedido", backref="pedido")
    total_pedido = Mapped[float] = mapped_column(nullable=False)
    status = Mapped[str] = mapped_column(nullable=False)
