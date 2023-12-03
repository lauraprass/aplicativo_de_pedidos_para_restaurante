from __future__ import annotations
from typing import List
from sqlalchemy import Column, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.config.base import Base

class ItemMenuPedido(Base):
    __tablename__ = 'item_menu_pedido'

    id = Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pedido_id = Mapped[int] = mapped_column(ForeignKey('pedido.id'))
    item_menu_id = Mapped[int] = mapped_column(ForeignKey('itemMenu.id'))
    quantidade = Mapped[int] = mapped_column(nullable=False)
