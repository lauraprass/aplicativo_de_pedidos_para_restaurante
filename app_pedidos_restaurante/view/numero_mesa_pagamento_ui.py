# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'numero_mesa_pagamento.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_Mesa(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(550, 494)
        self.widget_principal = QWidget(Dialog)
        self.widget_principal.setObjectName(u"widget_principal")
        self.widget_principal.setGeometry(QRect(10, 10, 531, 471))
        self.widget_principal.setStyleSheet(u"background-color: #588157; ")
        self.widget_logo = QWidget(self.widget_principal)
        self.widget_logo.setObjectName(u"widget_logo")
        self.widget_logo.setGeometry(QRect(200, 70, 74, 47))
        self.widget_logo.setMinimumSize(QSize(52, 25))
        self.verticalLayout_2 = QVBoxLayout(self.widget_logo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_logo = QLabel(self.widget_logo)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setMinimumSize(QSize(52, 25))
        self.lbl_logo.setStyleSheet(u"image: url(:/icon/Captura_de_tela_2023-12-05_203228-removebg-preview.png);")

        self.verticalLayout_2.addWidget(self.lbl_logo)

        self.widget_numero_mesa = QWidget(self.widget_principal)
        self.widget_numero_mesa.setObjectName(u"widget_numero_mesa")
        self.widget_numero_mesa.setGeometry(QRect(50, 170, 441, 91))
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
        self.widget_flor = QWidget(self.widget_principal)
        self.widget_flor.setObjectName(u"widget_flor")
        self.widget_flor.setGeometry(QRect(20, 410, 81, 41))
        self.lbl_flor = QLabel(self.widget_flor)
        self.lbl_flor.setObjectName(u"lbl_flor")
        self.lbl_flor.setGeometry(QRect(10, 10, 52, 25))
        self.lbl_flor.setMinimumSize(QSize(52, 25))
        self.lbl_flor.setStyleSheet(u"image: url(:/icon/healthy-living.png);")
        self.widget_flor_2 = QWidget(self.widget_principal)
        self.widget_flor_2.setObjectName(u"widget_flor_2")
        self.widget_flor_2.setGeometry(QRect(180, 410, 81, 41))
        self.lbl_flor_2 = QLabel(self.widget_flor_2)
        self.lbl_flor_2.setObjectName(u"lbl_flor_2")
        self.lbl_flor_2.setGeometry(QRect(10, 10, 52, 25))
        self.lbl_flor_2.setMinimumSize(QSize(52, 25))
        self.lbl_flor_2.setStyleSheet(u"image: url(:/icon/healthy-living.png);")
        self.widget_flor_3 = QWidget(self.widget_principal)
        self.widget_flor_3.setObjectName(u"widget_flor_3")
        self.widget_flor_3.setGeometry(QRect(330, 410, 81, 41))
        self.lbl_flor_3 = QLabel(self.widget_flor_3)
        self.lbl_flor_3.setObjectName(u"lbl_flor_3")
        self.lbl_flor_3.setGeometry(QRect(10, 10, 52, 25))
        self.lbl_flor_3.setMinimumSize(QSize(52, 25))
        self.lbl_flor_3.setStyleSheet(u"image: url(:/icon/healthy-living.png);")
        self.linha = QFrame(self.widget_principal)
        self.linha.setObjectName(u"linha")
        self.linha.setGeometry(QRect(-50, 150, 763, 3))
        self.linha.setFrameShape(QFrame.HLine)
        self.linha.setFrameShadow(QFrame.Sunken)
        self.widget_pagamento = QWidget(self.widget_principal)
        self.widget_pagamento.setObjectName(u"widget_pagamento")
        self.widget_pagamento.setGeometry(QRect(190, 10, 105, 43))
        self.verticalLayout = QVBoxLayout(self.widget_pagamento)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_pagamento = QLabel(self.widget_pagamento)
        self.lbl_pagamento.setObjectName(u"lbl_pagamento")
        self.lbl_pagamento.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout.addWidget(self.lbl_pagamento)

        self.widget_continuar = QWidget(self.widget_principal)
        self.widget_continuar.setObjectName(u"widget_continuar")
        self.widget_continuar.setGeometry(QRect(100, 290, 301, 81))
        self.btn_continuar = QPushButton(self.widget_continuar)
        self.btn_continuar.setObjectName(u"btn_continuar")
        self.btn_continuar.setGeometry(QRect(20, 10, 271, 61))
        self.btn_continuar.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_logo.setText("")
        self.lbl_numero_mesa.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Selecione o n\u00famero </span></p><p align=\"center\"><span style=\" font-weight:600;\">da mesa:</span></p></body></html>", None))
        self.lbl_flor.setText("")
        self.lbl_flor_2.setText("")
        self.lbl_flor_3.setText("")
        self.lbl_pagamento.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Pagamento</p></body></html>", None))
        self.btn_continuar.setText(QCoreApplication.translate("Dialog", u"Continuar", None))
    # retranslateUi

