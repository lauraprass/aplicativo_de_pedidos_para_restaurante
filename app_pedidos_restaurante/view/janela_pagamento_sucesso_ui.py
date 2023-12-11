# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_pagamento_sucesso.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)
import resource_rc

class PagamentoRealizado(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 364)
        self.widget_principal = QWidget(Dialog)
        self.widget_principal.setObjectName(u"widget_principal")
        self.widget_principal.setGeometry(QRect(10, 10, 371, 341))
        self.widget_principal.setStyleSheet(u"background-color: #588157; ")
        self.widget_realizado_sucesso = QWidget(self.widget_principal)
        self.widget_realizado_sucesso.setObjectName(u"widget_realizado_sucesso")
        self.widget_realizado_sucesso.setGeometry(QRect(20, 139, 311, 101))
        self.lbl_pagamento = QLabel(self.widget_realizado_sucesso)
        self.lbl_pagamento.setObjectName(u"lbl_pagamento")
        self.lbl_pagamento.setGeometry(QRect(10, 20, 291, 31))
        self.lbl_pagamento.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.lbl_pagamento_realizado_sucesso = QLabel(self.widget_realizado_sucesso)
        self.lbl_pagamento_realizado_sucesso.setObjectName(u"lbl_pagamento_realizado_sucesso")
        self.lbl_pagamento_realizado_sucesso.setGeometry(QRect(120, 60, 81, 31))
        self.lbl_pagamento_realizado_sucesso.setMinimumSize(QSize(52, 25))
        self.lbl_pagamento_realizado_sucesso.setStyleSheet(u"image: url(:/icon/check.png);")
        self.widget_logo = QWidget(self.widget_principal)
        self.widget_logo.setObjectName(u"widget_logo")
        self.widget_logo.setGeometry(QRect(20, 20, 341, 61))
        self.lbl_logo = QLabel(self.widget_logo)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setGeometry(QRect(140, 10, 61, 41))
        self.lbl_logo.setMinimumSize(QSize(52, 25))
        self.lbl_logo.setStyleSheet(u"image: url(:/icon/Captura_de_tela_2023-12-05_203228-removebg-preview.png);")
        self.widget_menu = QWidget(self.widget_principal)
        self.widget_menu.setObjectName(u"widget_menu")
        self.widget_menu.setGeometry(QRect(40, 270, 301, 51))
        self.lbl_menu_inicial = QLabel(self.widget_menu)
        self.lbl_menu_inicial.setObjectName(u"lbl_menu_inicial")
        self.lbl_menu_inicial.setGeometry(QRect(30, 9, 221, 31))
        self.lbl_menu_inicial.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_pagamento.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Pagamento realizado com sucesso!</p></body></html>", None))
        self.lbl_pagamento_realizado_sucesso.setText("")
        self.lbl_logo.setText("")
        self.lbl_menu_inicial.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Voltar Menu Inicial</p></body></html>", None))
    # retranslateUi

