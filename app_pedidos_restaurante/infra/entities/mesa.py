from __future__ import annotations
from typing import List
from sqlalchemy import Column, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.config.base import Base


class Mesa(Base):
    __tablename__ = 'mesa'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    numero_mesa: Mapped[int] = mapped_column(nullable=False)
    pedidos: relationship("Pedido", backref="mesa")

    def __init__(self, numero_mesa: int):
        self.numero_mesa = numero_mesa