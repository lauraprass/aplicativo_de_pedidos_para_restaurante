# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_pedido_realizado_sucesso.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)
import icon_rc

class Ui_Sucesso(object):
    def setupUi(self, Sucesso):
        if not Sucesso.objectName():
            Sucesso.setObjectName(u"Sucesso")
        Sucesso.resize(482, 424)
        self.widget_principal = QWidget(Sucesso)
        self.widget_principal.setObjectName(u"widget_principal")
        self.widget_principal.setGeometry(QRect(20, 20, 441, 381))
        self.widget_principal.setStyleSheet(u"background-color: #588157; ")
        self.widget_sucesso = QWidget(self.widget_principal)
        self.widget_sucesso.setObjectName(u"widget_sucesso")
        self.widget_sucesso.setGeometry(QRect(60, 90, 321, 161))
        self.lbl_sucesso = QLabel(self.widget_sucesso)
        self.lbl_sucesso.setObjectName(u"lbl_sucesso")
        self.lbl_sucesso.setGeometry(QRect(40, 20, 251, 41))
        self.lbl_sucesso.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.lbl_imagem_verificado = QLabel(self.widget_sucesso)
        self.lbl_imagem_verificado.setObjectName(u"lbl_imagem_verificado")
        self.lbl_imagem_verificado.setGeometry(QRect(120, 90, 101, 61))
        self.lbl_imagem_verificado.setMinimumSize(QSize(52, 25))
        self.lbl_imagem_verificado.setStyleSheet(u"image: url(:/icon/check.png);")
        self.widget_menu_inicial = QWidget(self.widget_principal)
        self.widget_menu_inicial.setObjectName(u"widget_menu_inicial")
        self.widget_menu_inicial.setGeometry(QRect(50, 290, 371, 61))
        self.btn_menu_inicial = QPushButton(self.widget_menu_inicial)
        self.btn_menu_inicial.setObjectName(u"btn_menu_inicial")
        self.btn_menu_inicial.setGeometry(QRect(20, 10, 331, 41))
        self.btn_menu_inicial.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.retranslateUi(Sucesso)

        QMetaObject.connectSlotsByName(Sucesso)
    # setupUi

    def retranslateUi(self, Sucesso):
        Sucesso.setWindowTitle(QCoreApplication.translate("Sucesso", u"Dialog", None))
        self.lbl_sucesso.setText(QCoreApplication.translate("Sucesso", u"<html><head/><body><p align=\"center\">Pedido realizado com sucesso!</p></body></html>", None))
        self.lbl_imagem_verificado.setText("")
        self.btn_menu_inicial.setText(QCoreApplication.translate("Sucesso", u"Voltar para Menu Inicial", None))
    # retranslateUi

