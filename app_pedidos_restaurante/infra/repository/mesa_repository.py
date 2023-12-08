from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from pedido_repository import PedidoRepository
Base = declarative_base()

class Mesa(Base):
    __tablename__ = 'mesas'
    id = Column (Integer, primary_key=True)
    numero = Column(Integer)
    pedidos = relationship('Pedido', back_populates='mesa')

class MesaRepository:
    @staticmethod
    def salvar(mesa):
        engine = create_engine('sqlite:///restaurante.db')
        Base.metadata.create_all(engine)
        session = Session(engine)

        session.add(mesa)
        session.commit()

        for pedido in mesa.pedidos:
            PedidoRepository.salvar(pedido, mesa.id)


    @staticmethod
    def buscarMesa():
        engine = create_engine('sqlite:///restaurante.db')
        Base.metadata.create_all(engine)
        session = Session(engine)

        mesa = session.query(Mesa).filter_by(numero=numero).first()

        if not mesa:
            return None

        for pedido_id in PedidoRepository.buscarIdsPorMesaId(mesa.id):
            pedido = PedidoRepository.buscarPorId(pedido_id)
            mesa.pedidos.append(pedido)
        return mesa