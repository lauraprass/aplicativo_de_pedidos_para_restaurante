# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_entradas.ui'
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
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_Entradas(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(802, 593)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_principal = QWidget(Dialog)
        self.widget_principal.setObjectName(u"widget_principal")
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
        self.widget_entradas.setGeometry(QRect(46, 10, 711, 48))
        self.layoutWidget = QWidget(self.widget_entradas)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(240, 10, 170, 28))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(52, 25))
        self.label.setStyleSheet(u"image: url(:/icon/Captura_de_tela_2023-12-05_203228-removebg-preview.png);")

        self.horizontalLayout.addWidget(self.label)

        self.lbl_entrada_2 = QLabel(self.layoutWidget)
        self.lbl_entrada_2.setObjectName(u"lbl_entrada_2")
        self.lbl_entrada_2.setStyleSheet(u"background-color: #588157; \n"
"font: 87 8pt \"Arial Black\";\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.lbl_entrada_2)

        self.widget_brusqueta = QWidget(self.widget_principal)
        self.widget_brusqueta.setObjectName(u"widget_brusqueta")
        self.widget_brusqueta.setGeometry(QRect(10, 90, 631, 161))
        self.lbl_info_brusqueta = QLabel(self.widget_brusqueta)
        self.lbl_info_brusqueta.setObjectName(u"lbl_info_brusqueta")
        self.lbl_info_brusqueta.setGeometry(QRect(180, 20, 211, 61))
        self.btn_adicionar_brusqueta = QPushButton(self.widget_brusqueta)
        self.btn_adicionar_brusqueta.setObjectName(u"btn_adicionar_brusqueta")
        self.btn_adicionar_brusqueta.setGeometry(QRect(510, 70, 101, 41))
        self.btn_adicionar_brusqueta.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.lbl_imagem_brusqueta = QLabel(self.widget_brusqueta)
        self.lbl_imagem_brusqueta.setObjectName(u"lbl_imagem_brusqueta")
        self.lbl_imagem_brusqueta.setGeometry(QRect(0, 10, 151, 141))
        self.lbl_imagem_brusqueta.setStyleSheet(u"image: url(:/icon/entrada brusqueta.png);")
        self.lbl_preco_brusqueta = QLabel(self.widget_brusqueta)
        self.lbl_preco_brusqueta.setObjectName(u"lbl_preco_brusqueta")
        self.lbl_preco_brusqueta.setGeometry(QRect(530, 10, 81, 31))
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
        self.widget_ostra = QWidget(self.widget_principal)
        self.widget_ostra.setObjectName(u"widget_ostra")
        self.widget_ostra.setGeometry(QRect(10, 250, 631, 181))
        self.lbl_imagem_ostra = QLabel(self.widget_ostra)
        self.lbl_imagem_ostra.setObjectName(u"lbl_imagem_ostra")
        self.lbl_imagem_ostra.setGeometry(QRect(10, 20, 151, 141))
        self.lbl_imagem_ostra.setStyleSheet(u"image: url(:/icon/ostra in natura.png);\n"
"")
        self.lbl_info_ostra = QLabel(self.widget_ostra)
        self.lbl_info_ostra.setObjectName(u"lbl_info_ostra")
        self.lbl_info_ostra.setGeometry(QRect(200, 40, 141, 61))
        self.btn_adicionar_ostra = QPushButton(self.widget_ostra)
        self.btn_adicionar_ostra.setObjectName(u"btn_adicionar_ostra")
        self.btn_adicionar_ostra.setGeometry(QRect(510, 90, 101, 41))
        self.btn_adicionar_ostra.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.lbl_preco_ostra = QLabel(self.widget_ostra)
        self.lbl_preco_ostra.setObjectName(u"lbl_preco_ostra")
        self.lbl_preco_ostra.setGeometry(QRect(530, 20, 81, 31))
        self.widget_ostra.raise_()
        self.widget_finalizar.raise_()
        self.widget_voltar.raise_()
        self.widget_brusqueta.raise_()
        self.linha_dois.raise_()
        self.linha_um.raise_()
        self.linha_tres.raise_()
        self.widget_entradas.raise_()

        self.verticalLayout.addWidget(self.widget_principal)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Entradas", None))
        self.label.setText("")
        self.lbl_entrada_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#005500;\">ENTRADAS</span></p></body></html>", None))
        self.lbl_info_brusqueta.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Brusquetas de ma\u00e7\u00e3 verde </span></p><p><span style=\" font-size:11pt;\">com queijo gorgonzola</span></p></body></html>", None))
        self.btn_adicionar_brusqueta.setText(QCoreApplication.translate("Dialog", u"Adicionar", None))
        self.lbl_imagem_brusqueta.setText("")
        self.lbl_preco_brusqueta.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">R$35,00</span></p></body></html>", None))
        self.btn_voltar_opcoes_menu.setText(QCoreApplication.translate("Dialog", u"Voltar para Op\u00e7\u00f5es Menu", None))
        self.btn_finalizar_pedido_entrada.setText(QCoreApplication.translate("Dialog", u"Finalizar Pedido", None))
        self.lbl_imagem_ostra.setText("")
        self.lbl_info_ostra.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Ostras In Natura</span></p><p><span style=\" font-size:11pt;\">(6 unidades)</span><br/></p></body></html>", None))
        self.btn_adicionar_ostra.setText(QCoreApplication.translate("Dialog", u"Adicionar", None))
        self.lbl_preco_ostra.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">R$45,00</span></p></body></html>", None))
    # retranslateUi

