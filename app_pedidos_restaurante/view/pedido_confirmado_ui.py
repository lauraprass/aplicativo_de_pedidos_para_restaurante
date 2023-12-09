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
from PySide6.QtWidgets import (QApplication, QDialog, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

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
        self.widget_confirmar_pedido.setGeometry(QRect(180, 449, 261, 91))
        self.btn_confirmar_pedido = QPushButton(self.widget_confirmar_pedido)
        self.btn_confirmar_pedido.setObjectName(u"btn_confirmar_pedido")
        self.btn_confirmar_pedido.setGeometry(QRect(20, 20, 221, 61))
        self.btn_confirmar_pedido.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.retranslateUi(ConfirmacaoPedido)

        QMetaObject.connectSlotsByName(ConfirmacaoPedido)
    # setupUi

    def retranslateUi(self, ConfirmacaoPedido):
        ConfirmacaoPedido.setWindowTitle(QCoreApplication.translate("ConfirmacaoPedido", u"Dialog", None))
        self.btn_confirmar_pedido.setText(QCoreApplication.translate("ConfirmacaoPedido", u"Confirmar Pedido", None))
    # retranslateUi

