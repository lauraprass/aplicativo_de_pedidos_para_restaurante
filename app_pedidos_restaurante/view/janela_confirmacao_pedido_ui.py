# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_confirmacao_pedido.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)

class Ui_ConfirmacaoPedido(object):
    def setupUi(self, ConfirmacaoPedido):
        if not ConfirmacaoPedido.objectName():
            ConfirmacaoPedido.setObjectName(u"ConfirmacaoPedido")
        ConfirmacaoPedido.resize(625, 609)
        self.widget_principal = QWidget(ConfirmacaoPedido)
        self.widget_principal.setObjectName(u"widget_principal")
        self.widget_principal.setGeometry(QRect(10, 10, 601, 581))
        self.widget_principal.setStyleSheet(u"background-color: #588157; ")
        self.widget_list_pedido = QWidget(self.widget_principal)
        self.widget_list_pedido.setObjectName(u"widget_list_pedido")
        self.widget_list_pedido.setGeometry(QRect(20, 30, 551, 361))
        self.list_pedido = QListWidget(self.widget_list_pedido)
        self.list_pedido.setObjectName(u"list_pedido")
        self.list_pedido.setGeometry(QRect(10, 10, 531, 351))
        self.widget_confirmar_pedido = QWidget(self.widget_principal)
        self.widget_confirmar_pedido.setObjectName(u"widget_confirmar_pedido")
        self.widget_confirmar_pedido.setGeometry(QRect(430, 510, 148, 43))
        self.horizontalLayout = QHBoxLayout(self.widget_confirmar_pedido)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_confirmar_pedido_2 = QPushButton(self.widget_confirmar_pedido)
        self.btn_confirmar_pedido_2.setObjectName(u"btn_confirmar_pedido_2")
        self.btn_confirmar_pedido_2.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.horizontalLayout.addWidget(self.btn_confirmar_pedido_2)

        self.widget_numero_mesa = QWidget(self.widget_principal)
        self.widget_numero_mesa.setObjectName(u"widget_numero_mesa")
        self.widget_numero_mesa.setGeometry(QRect(30, 409, 441, 91))
        self.txt_numero_mesa = QLineEdit(self.widget_numero_mesa)
        self.txt_numero_mesa.setObjectName(u"txt_numero_mesa")
        self.txt_numero_mesa.setGeometry(QRect(270, 20, 161, 41))
        self.lbl_numero_mesa = QLabel(self.widget_numero_mesa)
        self.lbl_numero_mesa.setObjectName(u"lbl_numero_mesa")
        self.lbl_numero_mesa.setGeometry(QRect(20, 20, 171, 61))
        self.lbl_numero_mesa.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.retranslateUi(ConfirmacaoPedido)

        QMetaObject.connectSlotsByName(ConfirmacaoPedido)
    # setupUi

    def retranslateUi(self, ConfirmacaoPedido):
        ConfirmacaoPedido.setWindowTitle(QCoreApplication.translate("ConfirmacaoPedido", u"Dialog", None))
        self.btn_confirmar_pedido_2.setText(QCoreApplication.translate("ConfirmacaoPedido", u"Confirmar Pedido", None))
        self.lbl_numero_mesa.setText(QCoreApplication.translate("ConfirmacaoPedido", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Selecione o n\u00famero </span></p><p align=\"center\"><span style=\" font-weight:600;\">da mesa:</span></p></body></html>", None))
    # retranslateUi

