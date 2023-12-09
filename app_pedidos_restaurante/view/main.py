import sys

from view.janela_bebidas_ui import Ui_Bebidas
from view.janela_opcoes_ui import Ui_Opcoes
from view.janela_cardapio_ui import Ui_Cardapio
from view.janela_entradas_ui import Ui_Entradas
from view.janela_pagamento_ui import Ui_Pagamento
from view.janela_opcoes_pagamento_ui import Ui_FormaPag
from view.janela_pratos_principais_ui import Ui_Pratos
from view.pagamento_realizado_ui import PagamentoRealizado
from infra.config.connection import DBConnectionHandler as db

from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QMessageBox, QFileDialog, QListWidget

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
        self.pedidoUi = PratosUi()
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
        self.btn_finalizar_pedido_entrada.clicked.connect(self.voltarMenu)
        self.btn_adicionar_caipirinha.clicked.connect()

    def voltarMenu(self):
        self.close()
        self.voltarMenuUi = MainWindow()
        self.voltarMenuUi.show()

class PratosUi(QDialog, Ui_Pratos):
    def __init__(self, parent=None):
        super(PratosUi, self).__init__(parent)
        self.setupUi(self)

        self.btn_voltar_opcoes_menu.clicked.connect(self.voltarMenu)
        self.btn_finalizar_pedido_entrada.clicked.connect(self.voltarMenu)

    def voltarMenu(self):
        self.close()
        self.voltarMenuUi = MainWindow()
        self.voltarMenuUi.show()

class EntradasUi(QDialog, Ui_Entradas):
    def __init__(self, parent=None):
        super(EntradasUi, self).__init__(parent)
        self.setupUi(self)

class PagamentosUi(QDialog, Ui_Pagamento):
    def __init__(self, parent=None):
        super(PagamentosUi, self).__init__(parent)
        self.setupUi(self)

        self.btn_voltar_menu_principal.clicked.connect(self.voltarMenu)
        self.btn_realizar_pagamento.clicked.connect(self.pagar)

    def voltarMenu(self):
        self.close()
        self.voltarMenuUi = MainWindow()
        self.voltarMenuUi.show()

    def pagar(self):
        self.close()
        self.mesaUi = FormaPag()
        self.mesaUi.show()

class FormaPag(QDialog, Ui_FormaPag):
    def __init__(self, parent=None):
        super(FormaPag, self).__init__(parent)
        self.setupUi(self)

    def pago(self):
        self.close()
        self.pagoUi = PagamentoOK()
        self.pagoUi.show()

class PagamentoOK(QDialog, PagamentoRealizado):
    def __init__(self, parent=None):
        super(PagamentoOK, self).__init__(parent)
        self.setupUi(self)

    # def



class Pagamento(QDialog, PagamentoRealizado):
    def __init__(self, parent=None):
        super(PagamentoRealizado, self).__init__(parent)
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication()
    model = QStandardItemModel()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())