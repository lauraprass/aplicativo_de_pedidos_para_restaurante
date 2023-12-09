# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_opcoes_pagamento.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QWidget)
import resource_rc

class Ui_FormaPag(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(657, 590)
        self.widget_principal = QWidget(Dialog)
        self.widget_principal.setObjectName(u"widget_principal")
        self.widget_principal.setGeometry(QRect(10, 20, 631, 551))
        self.widget_principal.setStyleSheet(u"background-color: #588157; ")
        self.widget_opcoes_pagamento = QWidget(self.widget_principal)
        self.widget_opcoes_pagamento.setObjectName(u"widget_opcoes_pagamento")
        self.widget_opcoes_pagamento.setGeometry(QRect(40, 50, 541, 81))
        self.radio_btn_inteiro = QRadioButton(self.widget_opcoes_pagamento)
        self.radio_btn_inteiro.setObjectName(u"radio_btn_inteiro")
        self.radio_btn_inteiro.setGeometry(QRect(20, 30, 171, 20))
        self.radio_btn_inteiro.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;")
        self.radio_btn_dividido = QRadioButton(self.widget_opcoes_pagamento)
        self.radio_btn_dividido.setObjectName(u"radio_btn_dividido")
        self.radio_btn_dividido.setGeometry(QRect(350, 30, 181, 20))
        self.radio_btn_dividido.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;")
        self.label = QLabel(self.widget_opcoes_pagamento)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 0, 61, 81))
        self.label.setStyleSheet(u"image: url(:/icon/pay-per-click.png);")
        self.widget_pix = QWidget(self.widget_principal)
        self.widget_pix.setObjectName(u"widget_pix")
        self.widget_pix.setGeometry(QRect(40, 290, 181, 151))
        self.btn_pix = QPushButton(self.widget_pix)
        self.btn_pix.setObjectName(u"btn_pix")
        self.btn_pix.setGeometry(QRect(10, 10, 161, 131))
        self.btn_pix.setStyleSheet(u"image: url(:/icon/1200px-Pix_logo.svg_.png);\n"
"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.linha = QFrame(self.widget_principal)
        self.linha.setObjectName(u"linha")
        self.linha.setGeometry(QRect(-30, 160, 763, 3))
        self.linha.setFrameShape(QFrame.HLine)
        self.linha.setFrameShadow(QFrame.Sunken)
        self.lbl_metodo_pagamento = QLabel(self.widget_principal)
        self.lbl_metodo_pagamento.setObjectName(u"lbl_metodo_pagamento")
        self.lbl_metodo_pagamento.setGeometry(QRect(140, 180, 371, 33))
        self.lbl_metodo_pagamento.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(20)
        self.lbl_metodo_pagamento.setFont(font)
        self.lbl_metodo_pagamento.setMouseTracking(True)
        self.lbl_metodo_pagamento.setText(u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#000000;\">Selecione o m\u00e9todo de pagamento:</span></p></body></html>")
        self.widget_cartao = QWidget(self.widget_principal)
        self.widget_cartao.setObjectName(u"widget_cartao")
        self.widget_cartao.setGeometry(QRect(240, 290, 181, 151))
        self.btn_cartao = QPushButton(self.widget_cartao)
        self.btn_cartao.setObjectName(u"btn_cartao")
        self.btn_cartao.setGeometry(QRect(10, 10, 161, 131))
        self.btn_cartao.setStyleSheet(u"image: url(:/icon/atm-card.png);\n"
"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.widget_dinheiro = QWidget(self.widget_principal)
        self.widget_dinheiro.setObjectName(u"widget_dinheiro")
        self.widget_dinheiro.setGeometry(QRect(440, 290, 181, 151))
        self.btn_dinheiro = QPushButton(self.widget_dinheiro)
        self.btn_dinheiro.setObjectName(u"btn_dinheiro")
        self.btn_dinheiro.setGeometry(QRect(0, 10, 161, 131))
        self.btn_dinheiro.setStyleSheet(u"image: url(:/icon/money.png);\n"
"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.radio_btn_inteiro.setText(QCoreApplication.translate("Dialog", u"Pagamento Inteiro", None))
        self.radio_btn_dividido.setText(QCoreApplication.translate("Dialog", u"Pagamento Dividido", None))
        self.label.setText("")
        self.btn_pix.setText("")
        self.btn_cartao.setText("")
        self.btn_dinheiro.setText("")
    # retranslateUi

