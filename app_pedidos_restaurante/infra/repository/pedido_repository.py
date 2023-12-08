from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from itemMenu_repository import itemMenuRepository

Base = declarative_base()

class Pedido(Base):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True)
    status = Column(String)
    total = Column(Float)
    mesa_id = Column(Integer, ForeignKey('mesas.id'))
    mesa = relationship('Mesa', back_populates='pedidos')
    itens = relationship('ItemMenu', secondary='itens_pedido')

class PedidoRepository:
    @staticmethod
    def salvar(pedido, mesa_id):
        engine = create_engine('sqlite:///restaurante.db')
        Base.metadata.create_all(engine)
        session = Session(engine)

        pedido.mesa_id = mesa_id
        session.add(pedido)
        session.commit()

        for item in pedido.itens:
            ItemMenuRepository.salvar(item, pedido.id)

    @staticmethod
    def buscarPorId(pedido_id):
        engine = create_engine('sqlite:///restaurante.db')
        Base.metadata.create_all(engine)
        session = Session(engine)

        pedido = session.query(Pedido).filter_by(id=pedido_id).first()

        if not pedido:
            return None

        for item_id in ItemMenuRepository.buscarIdsPorPedidoId(pedido_id):
            item = ItemMenuRepository.buscarPorId(item_id)
            pedido.itens.append(item)

        return pedido

    @staticmethod
    def buscarMesaPorId(mesa_id):
        engine = create_engine('sqlite:///restaurante.db')
        Base.metadata.create_all(engine)
        session = Session(engine)

        pedidos = session.query(Pedido.id).filter_by(mesa_id=mesa_id).all()
        return [pedido.id for pedido in pedidos]