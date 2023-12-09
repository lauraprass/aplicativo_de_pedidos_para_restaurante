# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_bebidas.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
import resource_rc
class Ui_Bebidas(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(861, 602)
        self.widget_principal = QWidget(Dialog)
        self.widget_principal.setObjectName(u"widget_principal")
        self.widget_principal.setGeometry(QRect(30, 10, 780, 571))
        self.widget_principal.setMaximumSize(QSize(16777215, 16777215))
        self.widget_principal.setStyleSheet(u"background-color: #588157; \n"
"")
        self.linha_dois = QFrame(self.widget_principal)
        self.linha_dois.setObjectName(u"linha_dois")
        self.linha_dois.setGeometry(QRect(0, 250, 763, 3))
        self.linha_dois.setFrameShape(QFrame.HLine)
        self.linha_dois.setFrameShadow(QFrame.Sunken)
        self.linha_um = QFrame(self.widget_principal)
        self.linha_um.setObjectName(u"linha_um")
        self.linha_um.setGeometry(QRect(0, 90, 763, 3))
        self.linha_um.setFrameShape(QFrame.HLine)
        self.linha_um.setFrameShadow(QFrame.Sunken)
        self.linha_tres = QFrame(self.widget_principal)
        self.linha_tres.setObjectName(u"linha_tres")
        self.linha_tres.setGeometry(QRect(0, 420, 763, 3))
        self.linha_tres.setFrameShape(QFrame.HLine)
        self.linha_tres.setFrameShadow(QFrame.Sunken)
        self.widget_entradas = QWidget(self.widget_principal)
        self.widget_entradas.setObjectName(u"widget_entradas")
        self.widget_entradas.setGeometry(QRect(90, 10, 607, 48))
        self.horizontalLayout = QHBoxLayout(self.widget_entradas)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(211, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lbl_entrada_2 = QLabel(self.widget_entradas)
        self.lbl_entrada_2.setObjectName(u"lbl_entrada_2")
        self.lbl_entrada_2.setStyleSheet(u"background-color: #588157; \n"
"font: 87 8pt \"Arial Black\";\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.lbl_entrada_2)

        self.horizontalSpacer_2 = QSpacerItem(248, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.widget_caipirinha = QWidget(self.widget_principal)
        self.widget_caipirinha.setObjectName(u"widget_caipirinha")
        self.widget_caipirinha.setGeometry(QRect(10, 90, 771, 161))
        self.lbl_titulo_caipirinha = QLabel(self.widget_caipirinha)
        self.lbl_titulo_caipirinha.setObjectName(u"lbl_titulo_caipirinha")
        self.lbl_titulo_caipirinha.setGeometry(QRect(220, 10, 211, 41))
        self.btn_adicionar_caipirinha = QPushButton(self.widget_caipirinha)
        self.btn_adicionar_caipirinha.setObjectName(u"btn_adicionar_caipirinha")
        self.btn_adicionar_caipirinha.setGeometry(QRect(640, 100, 101, 41))
        self.btn_adicionar_caipirinha.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.lbl_imagem_caipirinha = QLabel(self.widget_caipirinha)
        self.lbl_imagem_caipirinha.setObjectName(u"lbl_imagem_caipirinha")
        self.lbl_imagem_caipirinha.setGeometry(QRect(30, 10, 151, 141))
        self.lbl_imagem_caipirinha.setStyleSheet(u"image: url(:/icon/rapadura.png);\n"
"")
        self.lbl_preco_caipirinha = QLabel(self.widget_caipirinha)
        self.lbl_preco_caipirinha.setObjectName(u"lbl_preco_caipirinha")
        self.lbl_preco_caipirinha.setGeometry(QRect(650, 10, 81, 31))
        self.lbl_info_caipirinha = QLabel(self.widget_caipirinha)
        self.lbl_info_caipirinha.setObjectName(u"lbl_info_caipirinha")
        self.lbl_info_caipirinha.setGeometry(QRect(200, 60, 261, 61))
        self.widget_voltar = QWidget(self.widget_principal)
        self.widget_voltar.setObjectName(u"widget_voltar")
        self.widget_voltar.setGeometry(QRect(80, 450, 301, 80))
        self.btn_voltar_opcoes_menu = QPushButton(self.widget_voltar)
        self.btn_voltar_opcoes_menu.setObjectName(u"btn_voltar_opcoes_menu")
        self.btn_voltar_opcoes_menu.setGeometry(QRect(50, 10, 221, 61))
        self.btn_voltar_opcoes_menu.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.widget_finalizar = QWidget(self.widget_principal)
        self.widget_finalizar.setObjectName(u"widget_finalizar")
        self.widget_finalizar.setGeometry(QRect(400, 450, 251, 81))
        self.btn_finalizar_pedido_entrada = QPushButton(self.widget_finalizar)
        self.btn_finalizar_pedido_entrada.setObjectName(u"btn_finalizar_pedido_entrada")
        self.btn_finalizar_pedido_entrada.setGeometry(QRect(10, 10, 221, 61))
        self.btn_finalizar_pedido_entrada.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.widget_cerveja = QWidget(self.widget_principal)
        self.widget_cerveja.setObjectName(u"widget_cerveja")
        self.widget_cerveja.setGeometry(QRect(10, 250, 761, 181))
        self.lbl_imagem_cerveja = QLabel(self.widget_cerveja)
        self.lbl_imagem_cerveja.setObjectName(u"lbl_imagem_cerveja")
        self.lbl_imagem_cerveja.setGeometry(QRect(40, 20, 151, 141))
        self.lbl_imagem_cerveja.setStyleSheet(u"image: url(:/icon/cerveja.png);\n"
"")
        self.btn_adicionar_cerveja = QPushButton(self.widget_cerveja)
        self.btn_adicionar_cerveja.setObjectName(u"btn_adicionar_cerveja")
        self.btn_adicionar_cerveja.setGeometry(QRect(630, 110, 101, 41))
        self.btn_adicionar_cerveja.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.lbl_preco_cerveja = QLabel(self.widget_cerveja)
        self.lbl_preco_cerveja.setObjectName(u"lbl_preco_cerveja")
        self.lbl_preco_cerveja.setGeometry(QRect(650, 20, 81, 31))
        self.lbl_titulo_cerveja = QLabel(self.widget_cerveja)
        self.lbl_titulo_cerveja.setObjectName(u"lbl_titulo_cerveja")
        self.lbl_titulo_cerveja.setGeometry(QRect(240, 10, 211, 41))
        self.lbl_info_cerveja = QLabel(self.widget_cerveja)
        self.lbl_info_cerveja.setObjectName(u"lbl_info_cerveja")
        self.lbl_info_cerveja.setGeometry(QRect(210, 40, 301, 121))
        self.widget = QWidget(self.widget_principal)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(660, 440, 101, 101))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 101, 81))
        self.label.setStyleSheet(u"image: url(:/icon/Captura_de_tela_2023-12-05_203228-removebg-preview.png);")
        self.widget.raise_()
        self.widget_cerveja.raise_()
        self.widget_finalizar.raise_()
        self.widget_voltar.raise_()
        self.widget_caipirinha.raise_()
        self.linha_dois.raise_()
        self.linha_um.raise_()
        self.linha_tres.raise_()
        self.widget_entradas.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_entrada_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#005500;\">BEBIDAS</span></p></body></html>", None))
        self.lbl_titulo_caipirinha.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Caipirinha de rapadura de melado</span></p></body></html>", None))
        self.btn_adicionar_caipirinha.setText(QCoreApplication.translate("Dialog", u"Adicionar", None))
        self.lbl_imagem_caipirinha.setText("")
        self.lbl_preco_caipirinha.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">R$20,00</span></p></body></html>", None))
        self.lbl_info_caipirinha.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Cacha\u00e7a de alambique, lim\u00e3o, </span></p><p align=\"center\"><span style=\" font-size:11pt;\">cravo e rapadura de melado</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.btn_voltar_opcoes_menu.setText(QCoreApplication.translate("Dialog", u"Voltar para Op\u00e7\u00f5es Menu", None))
        self.btn_finalizar_pedido_entrada.setText(QCoreApplication.translate("Dialog", u"Finalizar Pedido", None))
        self.lbl_imagem_cerveja.setText("")
        self.btn_adicionar_cerveja.setText(QCoreApplication.translate("Dialog", u"Adicionar", None))
        self.lbl_preco_cerveja.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">R$30,00</span></p></body></html>", None))
        self.lbl_titulo_cerveja.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Cerveja Session IPA</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.lbl_info_cerveja.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">IPA com amargor equilibrado, </span></p><p align=\"center\"><span style=\" font-size:11pt;\">j\u00e1 no aroma, apresenta notas cr\u00edticas</span></p><p align=\"center\"><span style=\" font-size:11pt;\">de l\u00fapulos americanos que remetem</span></p><p align=\"center\"><span style=\" font-size:11pt;\">a frutas tropicais</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.label.setText("")
    # retranslateUi

