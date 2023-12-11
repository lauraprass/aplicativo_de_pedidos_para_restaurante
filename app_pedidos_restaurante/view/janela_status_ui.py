# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_status.ui'
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
    QPushButton, QSizePolicy, QWidget)
import resource_rc

class Ui_Status(object):
    def setupUi(self, Status):
        if not Status.objectName():
            Status.setObjectName(u"Status")
        Status.resize(618, 479)
        self.widget_principal = QWidget(Status)
        self.widget_principal.setObjectName(u"widget_principal")
        self.widget_principal.setGeometry(QRect(20, 20, 571, 441))
        self.widget_principal.setStyleSheet(u"background-color: #588157; ")
        self.widget_recebido = QWidget(self.widget_principal)
        self.widget_recebido.setObjectName(u"widget_recebido")
        self.widget_recebido.setGeometry(QRect(10, 130, 161, 171))
        self.lbl_recebido = QLabel(self.widget_recebido)
        self.lbl_recebido.setObjectName(u"lbl_recebido")
        self.lbl_recebido.setGeometry(QRect(10, 10, 141, 81))
        self.lbl_recebido.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.lbl_imagem_recebido = QLabel(self.widget_recebido)
        self.lbl_imagem_recebido.setObjectName(u"lbl_imagem_recebido")
        self.lbl_imagem_recebido.setGeometry(QRect(30, 100, 91, 61))
        self.lbl_imagem_recebido.setMinimumSize(QSize(52, 25))
        self.lbl_imagem_recebido.setStyleSheet(u"image: url(:/icon/chef.png);")
        self.widget_preparo = QWidget(self.widget_principal)
        self.widget_preparo.setObjectName(u"widget_preparo")
        self.widget_preparo.setGeometry(QRect(190, 130, 161, 171))
        self.lbl_preparo = QLabel(self.widget_preparo)
        self.lbl_preparo.setObjectName(u"lbl_preparo")
        self.lbl_preparo.setGeometry(QRect(0, 10, 141, 81))
        self.lbl_preparo.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.lbl_imagem_preparo = QLabel(self.widget_preparo)
        self.lbl_imagem_preparo.setObjectName(u"lbl_imagem_preparo")
        self.lbl_imagem_preparo.setGeometry(QRect(20, 100, 101, 61))
        self.lbl_imagem_preparo.setMinimumSize(QSize(52, 25))
        self.lbl_imagem_preparo.setStyleSheet(u"image: url(:/icon/cooking.png);")
        self.widget_servido = QWidget(self.widget_principal)
        self.widget_servido.setObjectName(u"widget_servido")
        self.widget_servido.setGeometry(QRect(370, 130, 161, 171))
        self.lbl_servido = QLabel(self.widget_servido)
        self.lbl_servido.setObjectName(u"lbl_servido")
        self.lbl_servido.setGeometry(QRect(10, 10, 141, 81))
        self.lbl_servido.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.lbl_imagem_servido = QLabel(self.widget_servido)
        self.lbl_imagem_servido.setObjectName(u"lbl_imagem_servido")
        self.lbl_imagem_servido.setGeometry(QRect(30, 110, 81, 41))
        self.lbl_imagem_servido.setMinimumSize(QSize(52, 25))
        self.lbl_imagem_servido.setStyleSheet(u"image: url(:/icon/tray.png);")
        self.widget_status = QWidget(self.widget_principal)
        self.widget_status.setObjectName(u"widget_status")
        self.widget_status.setGeometry(QRect(100, 30, 331, 51))
        self.lbl_status_pedido = QLabel(self.widget_status)
        self.lbl_status_pedido.setObjectName(u"lbl_status_pedido")
        self.lbl_status_pedido.setGeometry(QRect(100, 15, 171, 21))
        self.lbl_status_pedido.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.linha = QFrame(self.widget_principal)
        self.linha.setObjectName(u"linha")
        self.linha.setGeometry(QRect(-40, 120, 763, 3))
        self.linha.setFrameShape(QFrame.HLine)
        self.linha.setFrameShadow(QFrame.Sunken)
        self.widget_menu_inicial = QWidget(self.widget_principal)
        self.widget_menu_inicial.setObjectName(u"widget_menu_inicial")
        self.widget_menu_inicial.setGeometry(QRect(110, 350, 371, 61))
        self.btn_menu_inicial = QPushButton(self.widget_menu_inicial)
        self.btn_menu_inicial.setObjectName(u"btn_menu_inicial")
        self.btn_menu_inicial.setGeometry(QRect(20, 10, 331, 41))
        self.btn_menu_inicial.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.retranslateUi(Status)

        QMetaObject.connectSlotsByName(Status)
    # setupUi

    def retranslateUi(self, Status):
        Status.setWindowTitle(QCoreApplication.translate("Status", u"Dialog", None))
        self.lbl_recebido.setText(QCoreApplication.translate("Status", u"<html><head/><body><p align=\"center\">Recebido</p></body></html>", None))
        self.lbl_imagem_recebido.setText("")
        self.lbl_preparo.setText(QCoreApplication.translate("Status", u"<html><head/><body><p align=\"center\">Em</p><p align=\"center\">Preparo</p></body></html>", None))
        self.lbl_imagem_preparo.setText("")
        self.lbl_servido.setText(QCoreApplication.translate("Status", u"<html><head/><body><p align=\"center\">Servido</p></body></html>", None))
        self.lbl_imagem_servido.setText("")
        self.lbl_status_pedido.setText(QCoreApplication.translate("Status", u"<html><head/><body><p align=\"center\">Status do Pedido</p></body></html>", None))
        self.btn_menu_inicial.setText(QCoreApplication.translate("Status", u"Voltar para Menu Inicial", None))
    # retranslateUi

