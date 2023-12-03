from __future__ import annotations
from typing import List
from sqlalchemy import Column, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.config.base import Base


class itemMenu (Base):
    __tablename__ = 'itemMenu'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome_prato: Mapped[str] = mapped_column(nullable=False)
    ingredientes: Mapped[str] = mapped_column(nullable=False)
    preco: Mapped[float] = mapped_column(nullable=False)




