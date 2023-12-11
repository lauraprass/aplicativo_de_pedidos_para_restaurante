import sys

from view.janela_bebidas_ui import Ui_Bebidas
from view.janela_opcoes_ui import Ui_Opcoes
from view.janela_cardapio_ui import Ui_Cardapio
from view.janela_entradas_ui import Ui_Entradas
from view.janela_pagamento_ui import Ui_Pagamento
from view.janela_opcoes_pagamento_ui import Ui_FormaPag
from view.janela_pratos_principais_ui import Ui_Pratos
from view.janela_pagamento_sucesso_ui import PagamentoRealizado
from view.janela_status_ui import Ui_Status
from view.numero_mesa_pagamento_ui import Ui_Mesa
from view.numero_mesa_status_ui import Ui_MesaStatus
from view.janela_confirmacao_pedido_ui import Ui_ConfirmacaoPedido



from infra.config.connection import DBConnectionHandler as db

from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QMessageBox, QFileDialog, QListWidget, \
    QListWidgetItem


class MainWindow(QMainWindow, Ui_Opcoes):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        data_base = db

        self.btn_cardapio.clicked.connect(self.cardapio)
        self.btn_status.clicked.connect(self.acompanhar)
        self.btn_pagamento.clicked.connect(self.pagamento)

    def cardapio(self):
        self.close()
        self.UiCardapio = CardapioUi()
        self.UiCardapio.show()

    def acompanhar(self):
        self.close()
        self.pedidoUi = StatusUi()
        self.pedidoUi.show()

    def pagamento(self):
        self.close()
        self.pagamentoUi = PagamentosUi()
        self.pagamentoUi.show()

class CardapioUi(QDialog, Ui_Cardapio):
    def __init__(self, parent=None):
        super(CardapioUi, self).__init__(parent)
        self.setupUi(self)

        self.btn_cardapio_2.clicked.connect(self.entrada)
        self.btn_status_2.clicked.connect(self.pratos)
        self.btn_pagamento_2.clicked.connect(self.bebidas)
        self.btn_voltar_menu_principal.clicked.connect(self.voltarMenu)

    def entrada(self):
        self.close()
        self.entradaUi = EntradasUi()
        self.entradaUi.show()

    def pratos(self):
        self.close()
        self.pratosUi = PratosUi()
        self.pratosUi.show()

    def bebidas(self):
        self.close()
        self.bebidasUi = BebidasUi()
        self.bebidasUi.show()

    def voltarMenu(self):
        self.close()
        self.voltarMenuUi = MainWindow()
        self.voltarMenuUi.show()

class BebidasUi(QDialog, Ui_Bebidas):
    def __init__(self, parent=None):
        super(BebidasUi, self).__init__(parent)
        self.setupUi(self)

        self.btn_voltar_opcoes_menu.clicked.connect(self.voltarMenu)
        self.btn_finalizar_pedido_entrada.clicked.connect(self.confirmarPedido)
        self.btn_adicionar_caipirinha.clicked.connect(lambda: self.adicionarItem("Caipirinha"))
        self.btn_adicionar_cerveja.clicked.connect(lambda: self.adicionarItem("Cerveja"))

        self.itens_pedido = []

    def voltarMenu(self):
        self.close()
        self.voltarMenuUi = MainWindow()
        self.voltarMenuUi.show()

    def confirmarPedido(self):
        self.close()
        self.confirmarUi = ConfirmarUi(self.itens_pedido)
        self.confirmarUi.adicionarItens(self.itens_pedido)
        self.confirmarUi.show()

    def adicionarItem(self, item):
        self.itens_pedido.append(item)
        QMessageBox.information(self, "Sucesso", f"{item} adicionado com sucesso!")

class ConfirmarUi(QDialog, Ui_ConfirmacaoPedido):
    def __init__(self, pedido, parent=None):
        super(ConfirmarUi, self).__init__(parent)
        self.setupUi(self)
        self.pedido = pedido


        self.btn_confirmar_pedido_2.clicked.connect(self.confirmar)

    def adicionarItens(self, itens):
        # Adicione os itens à QListWidget
        for item in itens:
            list_item = QListWidgetItem(item)
            self.list_pedido.addItem(list_item)


    def confirmar(self):
        numero_mesa = self.txt_numero_mesa.text()
        if not self.txt_numero_mesa.text():
            QMessageBox.warning(self, "Erro", "Informe a mesa que deseja incluir")
            return

        mensagem = f"Pedido adicionado à mesa {numero_mesa} com sucesso!"
        QMessageBox.information(self, "Sucesso", mensagem)

        self.close()
        self.confirmarUi = MainWindow()
        self.confirmarUi.show()

# PratosUi
class PratosUi(QDialog, Ui_Pratos):
    def __init__(self, parent=None):
        super(PratosUi, self).__init__(parent)
        self.setupUi(self)

        self.btn_finalizar_pedido_entrada.clicked.connect(self.confirmarPedido)
        self.btn_voltar_opcoes_menu.clicked.connect(self.voltarMenu)
        self.btn_adicionar_camarao.clicked.connect(lambda: self.adicionarItem("Camarão"))
        self.btn_adicionar_guardado.clicked.connect(lambda: self.adicionarItem("Guardado"))

        # Adicione uma lista para armazenar os itens
        self.itens_pedido = []

    def voltarMenu(self):
        self.close()
        self.voltarMenuUi = MainWindow()
        self.voltarMenuUi.show()

    def confirmarPedido(self):
        # Passe a lista diretamente para a próxima tela (Ui_Confirmar)
        self.close()
        self.confirmarUi = ConfirmarUi(self.itens_pedido)
        self.confirmarUi.adicionarItens(self.itens_pedido)  # Adiciona os itens à lista na próxima tela
        self.confirmarUi.show()

    def adicionarItem(self, item):
        # Adicione o item à lista
        self.itens_pedido.append(item)

        # Exiba uma mensagem de sucesso
        QMessageBox.information(self, "Sucesso", f"{item} adicionado com sucesso!")



class MesaStatusUi(QDialog, Ui_MesaStatus):
    def __init__(self, parent=None):
        super(MesaStatusUi, self).__init__(parent)
        self.setupUi(self)

        self.btn_continuar.clicked.connect(self.proximo)

    def proximo(self):

        if not self.txt_numero_mesa.text():
            QMessageBox.warning(self, "Erro", "Informe a mesa que deseja consultar")
            return

        self.close()
        self.proximoUi = StatusUi()
        self.proximoUi.show()


class StatusUi(QDialog, Ui_Status):
    def __init__(self, parent=None):
        super(StatusUi, self).__init__(parent)
        self.setupUi(self)

        self.btn_menu_inicial.clicked.connect(self.voltarMenu)

    def voltarMenu(self):
        self.close()
        self.voltarMenuUi = MainWindow()
        self.voltarMenuUi.show()


class EntradasUi(QDialog, Ui_Entradas, Ui_ConfirmacaoPedido):
    def __init__(self, parent=None):
        super(EntradasUi, self).__init__(parent)
        self.setupUi(self)

        self.btn_voltar_opcoes_menu.clicked.connect(self.voltarMenu)
        self.btn_finalizar_pedido_entrada.clicked.connect(self.confirmarPedido)
        self.btn_adicionar_ostra.clicked.connect(lambda: self.adicionarItem("Ostra"))
        self.btn_adicionar_brusqueta.clicked.connect(lambda: self.adicionarItem("Brusqueta"))

        self.itens_pedido = []

    def voltarMenu(self):
        self.close()
        self.voltarMenuUi = MainWindow()
        self.voltarMenuUi.show()

    def confirmarPedido(self):

        self.close()
        self.confirmarUi = ConfirmarUi(self.itens_pedido)
        self.confirmarUi.adicionarItens(self.itens_pedido)
        self.confirmarUi.show()

    def adicionarItem(self, item):
        self.itens_pedido.append(item)
        QMessageBox.information(self, "Sucesso", f"{item} adicionado com sucesso!")


class PagamentosUi(QDialog, Ui_FormaPag):
    def __init__(self, parent=None):
        super(PagamentosUi, self).__init__(parent)
        self.setupUi(self)

        self.btn_pix.clicked.connect(self.pix)
        self.btn_cartao.clicked.connect(self.cartao)
        self.btn_dinheiro.clicked.connect(self.dinheiro)

    def pix(self):
        self.close()
        self.pixUi = PagamentoOK()
        self.pixUi.show()

    def dinheiro(self):
        self.close()
        self.dinheiroUi = PagamentoOK()
        self.dinheiroUi.show()

    def cartao(self):
        self.close()
        self.cartaoUi = PagamentoOK()
        self.cartaoUi.show()

    def voltarMenu(self):
        self.close()
        self.voltarMenuUi = MainWindow()
        self.voltarMenuUi.show()

class PagamentoOK(QDialog, PagamentoRealizado):
    def __init__(self, parent=None):
        super(PagamentoOK, self).__init__(parent)
        self.setupUi(self)

        # self.btn_?

    def voltarMenu(self):
        self.close()
        self.voltarMenuUi = MainWindow()
        self.voltarMenuUi.show()


if __name__ == '__main__':
    app = QApplication()
    model = QStandardItemModel()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())