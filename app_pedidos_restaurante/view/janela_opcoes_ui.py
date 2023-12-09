# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_opcoes.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_Opcoes(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(947, 719)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: #588157; \n"
"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_7 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(52, 25))
        self.widget_2.setStyleSheet(u"image: url(:/icon/Captura_de_tela_2023-12-05_203228-removebg-preview.png);")

        self.horizontalLayout_7.addWidget(self.widget_2)

        self.lbl_logo_3 = QLabel(self.widget)
        self.lbl_logo_3.setObjectName(u"lbl_logo_3")
        self.lbl_logo_3.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(20)
        self.lbl_logo_3.setFont(font)
        self.lbl_logo_3.setMouseTracking(True)
        self.lbl_logo_3.setText(u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#005500; vertical-align:super;\">Big Bamboo</span></p></body></html>")

        self.horizontalLayout_7.addWidget(self.lbl_logo_3)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_8 = QSpacerItem(98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalSpacer = QSpacerItem(18, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"image: url(:/icon/healthy-living.png);")

        self.horizontalLayout_6.addWidget(self.widget_3)

        self.lbl_opcao = QLabel(self.widget)
        self.lbl_opcao.setObjectName(u"lbl_opcao")
        self.lbl_opcao.setMaximumSize(QSize(16777215, 16777215))
        self.lbl_opcao.setFont(font)
        self.lbl_opcao.setMouseTracking(True)
        self.lbl_opcao.setText(u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#000000;\">Selecione o que voc\u00ea deseja:</span></p></body></html>")

        self.horizontalLayout_6.addWidget(self.lbl_opcao)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"image: url(:/icon/healthy-living.png);")

        self.horizontalLayout_6.addWidget(self.widget_4)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.linha = QFrame(self.widget)
        self.linha.setObjectName(u"linha")
        self.linha.setFrameShape(QFrame.HLine)
        self.linha.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.linha)

        self.verticalSpacer_2 = QSpacerItem(15, 98, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_cardapio = QWidget(self.widget)
        self.widget_cardapio.setObjectName(u"widget_cardapio")
        self.verticalLayout_3 = QVBoxLayout(self.widget_cardapio)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_cardapio = QPushButton(self.widget_cardapio)
        self.btn_cardapio.setObjectName(u"btn_cardapio")
        self.btn_cardapio.setMinimumSize(QSize(181, 161))
        palette = QPalette()
        brush = QBrush(QColor(173, 193, 120, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_cardapio.setPalette(palette)
        self.btn_cardapio.setStyleSheet(u"background-color: #adc178; \n"
"image: url(:/icon/balanced-diet.png);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout_3.addWidget(self.btn_cardapio)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lbl_cardapio = QLabel(self.widget_cardapio)
        self.lbl_cardapio.setObjectName(u"lbl_cardapio")
        self.lbl_cardapio.setStyleSheet(u"background-color: #588157; \n"
"font: 87 8pt \"Arial Black\";\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.lbl_cardapio)

        self.horizontalSpacer_2 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.horizontalLayout_5.addWidget(self.widget_cardapio)

        self.widget_status = QWidget(self.widget)
        self.widget_status.setObjectName(u"widget_status")
        self.verticalLayout_4 = QVBoxLayout(self.widget_status)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_status = QPushButton(self.widget_status)
        self.btn_status.setObjectName(u"btn_status")
        self.btn_status.setMinimumSize(QSize(181, 161))
        self.btn_status.setStyleSheet(u"background-color: #adc178; \n"
"image: url(:/icon/nutrition.png);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout_4.addWidget(self.btn_status)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.lbl_status = QLabel(self.widget_status)
        self.lbl_status.setObjectName(u"lbl_status")
        self.lbl_status.setStyleSheet(u"background-color: #588157	; \n"
"font: 87 8pt \"Arial Black\";")

        self.horizontalLayout_3.addWidget(self.lbl_status)

        self.horizontalSpacer_4 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addWidget(self.widget_status)

        self.widget_pagamento = QWidget(self.widget)
        self.widget_pagamento.setObjectName(u"widget_pagamento")
        self.verticalLayout_5 = QVBoxLayout(self.widget_pagamento)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_pagamento = QPushButton(self.widget_pagamento)
        self.btn_pagamento.setObjectName(u"btn_pagamento")
        self.btn_pagamento.setMinimumSize(QSize(181, 161))
        self.btn_pagamento.setStyleSheet(u"background-color: #adc178; \n"
"image: url(:/icon/debit-card (1).png);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout_5.addWidget(self.btn_pagamento)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.label_pagamento = QLabel(self.widget_pagamento)
        self.label_pagamento.setObjectName(u"label_pagamento")
        self.label_pagamento.setStyleSheet(u"background-color: #588157	; \n"
"font: 87 8pt \"Arial Black\";")

        self.horizontalLayout_4.addWidget(self.label_pagamento)

        self.horizontalSpacer_6 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addWidget(self.widget_pagamento)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.btn_voltar_menu_inicial = QPushButton(self.widget)
        self.btn_voltar_menu_inicial.setObjectName(u"btn_voltar_menu_inicial")
        self.btn_voltar_menu_inicial.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout.addWidget(self.btn_voltar_menu_inicial)

        self.verticalSpacer_3 = QSpacerItem(18, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.linha.raise_()
        self.btn_voltar_menu_inicial.raise_()

        self.verticalLayout_2.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
#if QT_CONFIG(tooltip)
        self.widget_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icon/restaurant.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_cardapio.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; color:#aa0000;\">CARD\u00c1PIO</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cardapio.setText("")
        self.lbl_cardapio.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#005500;\">CARD\u00c1PIO</span><span style=\" color:#005500;\"/></p></body></html>", None))
        self.btn_status.setText("")
        self.lbl_status.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#005500;\">ACOMPANHAR</span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#005500;\">PEDIDO</span></p></body></html>", None))
        self.btn_pagamento.setText("")
        self.label_pagamento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#005500;\">PAGAMENTO</span></p></body></html>", None))
        self.btn_voltar_menu_inicial.setText(QCoreApplication.translate("MainWindow", u"Voltar Menu Incial", None))
    # retranslateUi

