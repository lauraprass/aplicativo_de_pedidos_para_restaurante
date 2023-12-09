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
        Dialog.resize(400, 300)
        self.widget_principal = QWidget(Dialog)
        self.widget_principal.setObjectName(u"widget_principal")
        self.widget_principal.setGeometry(QRect(10, 10, 371, 281))
        self.widget_principal.setStyleSheet(u"background-color: #588157; ")
        self.widget_2 = QWidget(self.widget_principal)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 139, 311, 101))
        self.lbl_pagamento = QLabel(self.widget_2)
        self.lbl_pagamento.setObjectName(u"lbl_pagamento")
        self.lbl_pagamento.setGeometry(QRect(10, 20, 291, 31))
        self.lbl_pagamento.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 60, 81, 31))
        self.label_2.setMinimumSize(QSize(52, 25))
        self.label_2.setStyleSheet(u"image: url(:/icon/check.png);")
        self.widget = QWidget(self.widget_principal)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 341, 61))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 10, 61, 41))
        self.label.setMinimumSize(QSize(52, 25))
        self.label.setStyleSheet(u"image: url(:/icon/Captura_de_tela_2023-12-05_203228-removebg-preview.png);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_pagamento.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Pagamento realizado com sucesso!</p></body></html>", None))
        self.label_2.setText("")
        self.label.setText("")
    # retranslateUi

