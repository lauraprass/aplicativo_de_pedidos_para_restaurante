# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_pagamento.ui'
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
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)
import resource_rc

class Ui_Pagamento(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(750, 651)
        self.widget_principal = QWidget(Dialog)
        self.widget_principal.setObjectName(u"widget_principal")
        self.widget_principal.setGeometry(QRect(40, 40, 641, 601))
        self.widget_principal.setStyleSheet(u"background-color: #588157; ")
        self.widget_list_conta = QWidget(self.widget_principal)
        self.widget_list_conta.setObjectName(u"widget_list_conta")
        self.widget_list_conta.setGeometry(QRect(10, 10, 551, 361))
        self.list_conta = QListWidget(self.widget_list_conta)
        self.list_conta.setObjectName(u"list_conta")
        self.list_conta.setGeometry(QRect(10, 10, 531, 351))
        self.widget_voltar = QWidget(self.widget_principal)
        self.widget_voltar.setObjectName(u"widget_voltar")
        self.widget_voltar.setGeometry(QRect(60, 500, 241, 80))
        self.btn_voltar_menu_principal = QPushButton(self.widget_voltar)
        self.btn_voltar_menu_principal.setObjectName(u"btn_voltar_menu_principal")
        self.btn_voltar_menu_principal.setGeometry(QRect(10, 10, 221, 61))
        self.btn_voltar_menu_principal.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.widget_realiza_pagamento = QWidget(self.widget_principal)
        self.widget_realiza_pagamento.setObjectName(u"widget_realiza_pagamento")
        self.widget_realiza_pagamento.setGeometry(QRect(350, 500, 241, 80))
        self.btn_realizar_pagamento = QPushButton(self.widget_realiza_pagamento)
        self.btn_realizar_pagamento.setObjectName(u"btn_realizar_pagamento")
        self.btn_realizar_pagamento.setGeometry(QRect(10, 10, 221, 61))
        self.btn_realizar_pagamento.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.linha = QFrame(self.widget_principal)
        self.linha.setObjectName(u"linha")
        self.linha.setGeometry(QRect(-10, 480, 763, 3))
        self.linha.setFrameShape(QFrame.HLine)
        self.linha.setFrameShadow(QFrame.Sunken)
        self.lbl_flor = QLabel(self.widget_principal)
        self.lbl_flor.setObjectName(u"lbl_flor")
        self.lbl_flor.setGeometry(QRect(580, 10, 61, 31))
        self.lbl_flor.setStyleSheet(u"image: url(:/icon/healthy-living.png);")
        self.lbl_flor_tres = QLabel(self.widget_principal)
        self.lbl_flor_tres.setObjectName(u"lbl_flor_tres")
        self.lbl_flor_tres.setGeometry(QRect(580, 300, 61, 31))
        self.lbl_flor_tres.setStyleSheet(u"image: url(:/icon/healthy-living.png);")
        self.lbl_logo = QLabel(self.widget_principal)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setGeometry(QRect(570, 70, 71, 51))
        self.lbl_logo.setStyleSheet(u"image: url(:/icon/Captura_de_tela_2023-12-05_203228-removebg-preview.png);")
        self.lbl_flor_dois = QLabel(self.widget_principal)
        self.lbl_flor_dois.setObjectName(u"lbl_flor_dois")
        self.lbl_flor_dois.setGeometry(QRect(580, 150, 61, 31))
        self.lbl_flor_dois.setStyleSheet(u"image: url(:/icon/healthy-living.png);")
        self.lbl_logo_dois = QLabel(self.widget_principal)
        self.lbl_logo_dois.setObjectName(u"lbl_logo_dois")
        self.lbl_logo_dois.setGeometry(QRect(570, 220, 71, 51))
        self.lbl_logo_dois.setStyleSheet(u"image: url(:/icon/Captura_de_tela_2023-12-05_203228-removebg-preview.png);")
        self.widget = QWidget(self.widget_principal)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(210, 390, 371, 80))
        self.lbl_total_conta = QLabel(self.widget)
        self.lbl_total_conta.setObjectName(u"lbl_total_conta")
        self.lbl_total_conta.setGeometry(QRect(10, 10, 341, 51))
        self.lbl_total_conta.setStyleSheet(u"background-color: #588157; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")
        self.txt_total_conta = QLineEdit(self.widget)
        self.txt_total_conta.setObjectName(u"txt_total_conta")
        self.txt_total_conta.setGeometry(QRect(82, 21, 251, 31))
        self.txt_total_conta.setStyleSheet(u"background-color: #adc178; ")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_voltar_menu_principal.setText(QCoreApplication.translate("Dialog", u"Voltar para Menu Principal", None))
        self.btn_realizar_pagamento.setText(QCoreApplication.translate("Dialog", u"Realizar Pagamento", None))
        self.lbl_flor.setText("")
        self.lbl_flor_tres.setText("")
        self.lbl_logo.setText("")
        self.lbl_flor_dois.setText("")
        self.lbl_logo_dois.setText("")
        self.lbl_total_conta.setText(QCoreApplication.translate("Dialog", u"Total:", None))
    # retranslateUi

