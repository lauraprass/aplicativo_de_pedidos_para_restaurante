# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'numero_mesa_status.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)
import resource_rc

class Ui_MesaStatus(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(552, 543)
        self.widget_principal = QWidget(Dialog)
        self.widget_principal.setObjectName(u"widget_principal")
        self.widget_principal.setGeometry(QRect(20, 20, 501, 511))
        self.widget_principal.setStyleSheet(u"background-color: #588157; ")
        self.widget_status = QWidget(self.widget_principal)
        self.widget_status.setObjectName(u"widget_status")
        self.widget_status.setGeometry(QRect(40, 20, 331, 51))
        self.lbl_status_pedido = QLabel(self.widget_status)
        self.lbl_status_pedido.setObjectName(u"lbl_status_pedido")
        self.lbl_status_pedido.setGeometry(QRect(100, 15, 171, 21))
        self.lbl_status_pedido.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.widget_numero_mesa = QWidget(self.widget_principal)
        self.widget_numero_mesa.setObjectName(u"widget_numero_mesa")
        self.widget_numero_mesa.setGeometry(QRect(20, 240, 441, 91))
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
        self.widget_logo = QWidget(self.widget_principal)
        self.widget_logo.setObjectName(u"widget_logo")
        self.widget_logo.setGeometry(QRect(180, 80, 121, 71))
        self.horizontalLayout = QHBoxLayout(self.widget_logo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_logo = QLabel(self.widget_logo)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setMinimumSize(QSize(52, 25))
        self.lbl_logo.setStyleSheet(u"image: url(:/icon/Captura_de_tela_2023-12-05_203228-removebg-preview.png);")

        self.horizontalLayout.addWidget(self.lbl_logo)

        self.linha = QFrame(self.widget_principal)
        self.linha.setObjectName(u"linha")
        self.linha.setGeometry(QRect(-50, 180, 763, 3))
        self.linha.setFrameShape(QFrame.HLine)
        self.linha.setFrameShadow(QFrame.Sunken)
        self.widget_flor = QWidget(self.widget_principal)
        self.widget_flor.setObjectName(u"widget_flor")
        self.widget_flor.setGeometry(QRect(50, 450, 81, 41))
        self.lbl_flor = QLabel(self.widget_flor)
        self.lbl_flor.setObjectName(u"lbl_flor")
        self.lbl_flor.setGeometry(QRect(10, 10, 52, 25))
        self.lbl_flor.setMinimumSize(QSize(52, 25))
        self.lbl_flor.setStyleSheet(u"image: url(:/icon/healthy-living.png);")
        self.widget_flor_2 = QWidget(self.widget_principal)
        self.widget_flor_2.setObjectName(u"widget_flor_2")
        self.widget_flor_2.setGeometry(QRect(180, 450, 81, 41))
        self.lbl_flor_2 = QLabel(self.widget_flor_2)
        self.lbl_flor_2.setObjectName(u"lbl_flor_2")
        self.lbl_flor_2.setGeometry(QRect(10, 10, 52, 25))
        self.lbl_flor_2.setMinimumSize(QSize(52, 25))
        self.lbl_flor_2.setStyleSheet(u"image: url(:/icon/healthy-living.png);")
        self.widget_flor_3 = QWidget(self.widget_principal)
        self.widget_flor_3.setObjectName(u"widget_flor_3")
        self.widget_flor_3.setGeometry(QRect(320, 450, 81, 41))
        self.lbl_flor_3 = QLabel(self.widget_flor_3)
        self.lbl_flor_3.setObjectName(u"lbl_flor_3")
        self.lbl_flor_3.setGeometry(QRect(10, 10, 52, 25))
        self.lbl_flor_3.setMinimumSize(QSize(52, 25))
        self.lbl_flor_3.setStyleSheet(u"image: url(:/icon/healthy-living.png);")
        self.widget_continuar = QWidget(self.widget_principal)
        self.widget_continuar.setObjectName(u"widget_continuar")
        self.widget_continuar.setGeometry(QRect(100, 350, 301, 81))
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
        self.lbl_status_pedido.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Status do Pedido</p></body></html>", None))
        self.lbl_numero_mesa.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Selecione o n\u00famero </span></p><p align=\"center\"><span style=\" font-weight:600;\">da mesa:</span></p></body></html>", None))
        self.lbl_logo.setText("")
        self.lbl_flor.setText("")
        self.lbl_flor_2.setText("")
        self.lbl_flor_3.setText("")
        self.btn_continuar.setText(QCoreApplication.translate("Dialog", u"Continuar", None))
    # retranslateUi

