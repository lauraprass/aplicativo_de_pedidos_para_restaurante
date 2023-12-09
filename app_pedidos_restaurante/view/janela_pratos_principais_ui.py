# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_pratos_principais.ui'
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

class Ui_Pratos(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(807, 589)
        self.widget_principal = QWidget(Dialog)
        self.widget_principal.setObjectName(u"widget_principal")
        self.widget_principal.setGeometry(QRect(10, 10, 780, 571))
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
        self.widget_pratos = QWidget(self.widget_principal)
        self.widget_pratos.setObjectName(u"widget_pratos")
        self.widget_pratos.setGeometry(QRect(16, 10, 741, 48))
        self.layoutWidget = QWidget(self.widget_pratos)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 10, 735, 28))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(211, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(52, 25))
        self.label.setStyleSheet(u"image: url(:/icon/Captura_de_tela_2023-12-05_203228-removebg-preview.png);")

        self.horizontalLayout.addWidget(self.label)

        self.lbl_pratos = QLabel(self.layoutWidget)
        self.lbl_pratos.setObjectName(u"lbl_pratos")
        self.lbl_pratos.setStyleSheet(u"background-color: #588157; \n"
"font: 87 8pt \"Arial Black\";\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.lbl_pratos)

        self.horizontalSpacer_2 = QSpacerItem(248, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.widget_camarao_moranga = QWidget(self.widget_principal)
        self.widget_camarao_moranga.setObjectName(u"widget_camarao_moranga")
        self.widget_camarao_moranga.setGeometry(QRect(30, 90, 731, 161))
        self.lbl_info_camarao = QLabel(self.widget_camarao_moranga)
        self.lbl_info_camarao.setObjectName(u"lbl_info_camarao")
        self.lbl_info_camarao.setGeometry(QRect(180, 60, 371, 91))
        self.btn_adicionar_camarao = QPushButton(self.widget_camarao_moranga)
        self.btn_adicionar_camarao.setObjectName(u"btn_adicionar_camarao")
        self.btn_adicionar_camarao.setGeometry(QRect(620, 100, 101, 41))
        self.btn_adicionar_camarao.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.lbl_preco_camarao = QLabel(self.widget_camarao_moranga)
        self.lbl_preco_camarao.setObjectName(u"lbl_preco_camarao")
        self.lbl_preco_camarao.setGeometry(QRect(630, 10, 81, 31))
        self.lbl_foto_camarao = QLabel(self.widget_camarao_moranga)
        self.lbl_foto_camarao.setObjectName(u"lbl_foto_camarao")
        self.lbl_foto_camarao.setGeometry(QRect(30, 10, 131, 141))
        self.lbl_foto_camarao.setStyleSheet(u"image: url(:/icon/prato 2.png);")
        self.lbl_titulo_camarao = QLabel(self.widget_camarao_moranga)
        self.lbl_titulo_camarao.setObjectName(u"lbl_titulo_camarao")
        self.lbl_titulo_camarao.setGeometry(QRect(250, 10, 211, 31))
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
        self.widget_guardado = QWidget(self.widget_principal)
        self.widget_guardado.setObjectName(u"widget_guardado")
        self.widget_guardado.setGeometry(QRect(30, 250, 731, 181))
        self.btn_adicionar_guardado = QPushButton(self.widget_guardado)
        self.btn_adicionar_guardado.setObjectName(u"btn_adicionar_guardado")
        self.btn_adicionar_guardado.setGeometry(QRect(620, 110, 101, 41))
        self.btn_adicionar_guardado.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.lbl_foto_guardado = QLabel(self.widget_guardado)
        self.lbl_foto_guardado.setObjectName(u"lbl_foto_guardado")
        self.lbl_foto_guardado.setGeometry(QRect(30, 10, 141, 151))
        self.lbl_foto_guardado.setStyleSheet(u"image: url(:/icon/guardado.png);")
        self.lbl_titulo_guardado = QLabel(self.widget_guardado)
        self.lbl_titulo_guardado.setObjectName(u"lbl_titulo_guardado")
        self.lbl_titulo_guardado.setGeometry(QRect(240, 10, 211, 31))
        self.lbl_info_guardado = QLabel(self.widget_guardado)
        self.lbl_info_guardado.setObjectName(u"lbl_info_guardado")
        self.lbl_info_guardado.setGeometry(QRect(190, 50, 371, 91))
        self.lbl_preco_guardado = QLabel(self.widget_guardado)
        self.lbl_preco_guardado.setObjectName(u"lbl_preco_guardado")
        self.lbl_preco_guardado.setGeometry(QRect(630, 10, 81, 31))
        self.widget_guardado.raise_()
        self.widget_finalizar.raise_()
        self.widget_voltar.raise_()
        self.widget_camarao_moranga.raise_()
        self.linha_dois.raise_()
        self.linha_um.raise_()
        self.linha_tres.raise_()
        self.widget_pratos.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.lbl_pratos.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#005500;\">PRATOS PRINCIPAIS</span></p></body></html>", None))
        self.lbl_info_camarao.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Moranga recheada com camar\u00f5es refogados</span></p><p align=\"center\"><span style=\" font-size:10pt;\">e requeij\u00e3o cremoso, acompanha arroz, batatas</span></p><p align=\"center\"><span style=\" font-size:10pt;\">fritas r\u00fasticas e salada org\u00e2nica</span></p></body></html>", None))
        self.btn_adicionar_camarao.setText(QCoreApplication.translate("Dialog", u"Adicionar", None))
        self.lbl_preco_camarao.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">R$190,00</span></p></body></html>", None))
        self.lbl_foto_camarao.setText("")
        self.lbl_titulo_camarao.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Camar\u00e3o na moranga</span></p></body></html>", None))
        self.btn_voltar_opcoes_menu.setText(QCoreApplication.translate("Dialog", u"Voltar para Op\u00e7\u00f5es Menu", None))
        self.btn_finalizar_pedido_entrada.setText(QCoreApplication.translate("Dialog", u"Finalizar Pedido", None))
        self.btn_adicionar_guardado.setText(QCoreApplication.translate("Dialog", u"Adicionar", None))
        self.lbl_foto_guardado.setText("")
        self.lbl_titulo_guardado.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Guardado do Emba\u00fa</span></p></body></html>", None))
        self.lbl_info_guardado.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Camar\u00f5es refogados com tomate e cebola,</span></p><p align=\"center\"><span style=\" font-size:10pt;\">pur\u00ea de aipim com queijo gratinado e fil\u00e9 de peixe</span></p><p align=\"center\"><span style=\" font-size:10pt;\">nobre. Acompanha arroz e salada org\u00e2nica.</span></p></body></html>", None))
        self.lbl_preco_guardado.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">R$200,00</span></p></body></html>", None))
    # retranslateUi

