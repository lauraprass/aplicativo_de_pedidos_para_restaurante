from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class ItemMenu(Base):
    __tablename__ = 'itens_menu'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    preco = Column(Float)
    ingredientes = Column(String)

class itemMenuRepository:
    @staticmethod
    def  salvar(item, pedido_id):
        engine = create_engine('sqlite:///restaurante.db')
        Base.metadata.create_all(engine)
        session = Session(engine)

        session.add(item)
        session.commit()

        session.execute("INSERT INTO itens_pedido (pedido_id, item_id) VALUES (?, ?)",
                        (pedido_id, item.id))
        session.commit()

    @staticmethod
    def buscarPorId(item_id):
        engine = create_engine('sqlite:///restaurante.db')
        Base.metadata.create_all(engine)
        session = Session(engine)

        item = session.query(ItemMenu).filter_by(id=item_id).first()

        return item

    @staticmethod
    def buscarIdsPorPedidoId(pedido_id):
        engine = create_engine('sqlite:///restaurante.db')
        Base.metadata.create_all(engine)
        session = Session(engine)

        itens = session.execute("SELECT item_id FROM itens_pedido WHERE pedido_id=?", (pedido_id,)).fetchall()

        return [item.id for item in itens]