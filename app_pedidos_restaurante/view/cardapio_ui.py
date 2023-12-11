# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_cardapio.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import icon_rc

class Ui_Dialog_cardapio(object):
    def setupUi(self, Dialog_cardapio):
        if not Dialog_cardapio.objectName():
            Dialog_cardapio.setObjectName(u"Dialog_cardapio")
        Dialog_cardapio.resize(686, 526)
        self.horizontalLayout = QHBoxLayout(Dialog_cardapio)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.central_widget = QWidget(Dialog_cardapio)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"background-color: #588157; \n"
"")
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_11 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_7 = QWidget(self.central_widget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(52, 25))
        self.widget_7.setMaximumSize(QSize(52, 25))
        self.widget_7.setStyleSheet(u"image: url(:/icon/Captura_de_tela_2023-12-05_203228-removebg-preview.png);")

        self.horizontalLayout_3.addWidget(self.widget_7)

        self.lbl_logo = QLabel(self.central_widget)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(20)
        self.lbl_logo.setFont(font)
        self.lbl_logo.setMouseTracking(True)
        self.lbl_logo.setText(u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#005500; vertical-align:super;\">Big Bamboo</span></p></body></html>")

        self.horizontalLayout_3.addWidget(self.lbl_logo)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_12 = QSpacerItem(98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_12)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget_8 = QWidget(self.central_widget)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"image: url(:/icon/healthy-living.png);")

        self.horizontalLayout_13.addWidget(self.widget_8)

        self.lbl_opcao_2 = QLabel(self.central_widget)
        self.lbl_opcao_2.setObjectName(u"lbl_opcao_2")
        self.lbl_opcao_2.setMaximumSize(QSize(16777215, 16777215))
        self.lbl_opcao_2.setFont(font)
        self.lbl_opcao_2.setMouseTracking(True)
        self.lbl_opcao_2.setText(u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#000000;\">Selecione o que voc\u00ea deseja:</span></p></body></html>")

        self.horizontalLayout_13.addWidget(self.lbl_opcao_2)

        self.widget_9 = QWidget(self.central_widget)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"image: url(:/icon/healthy-living.png);")

        self.horizontalLayout_13.addWidget(self.widget_9)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.widget_opcao_3 = QWidget(self.central_widget)
        self.widget_opcao_3.setObjectName(u"widget_opcao_3")
        self.widget_opcao_3.setMinimumSize(QSize(570, 0))
        self.widget_opcao_3.setStyleSheet(u"image: url(:/icon/healthy-living.png);")

        self.verticalLayout.addWidget(self.widget_opcao_3)

        self.linha_2 = QFrame(self.central_widget)
        self.linha_2.setObjectName(u"linha_2")
        self.linha_2.setFrameShape(QFrame.HLine)
        self.linha_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.linha_2)

        self.verticalSpacer_5 = QSpacerItem(18, 59, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.widget_cardapio_2 = QWidget(self.central_widget)
        self.widget_cardapio_2.setObjectName(u"widget_cardapio_2")
        self.verticalLayout_6 = QVBoxLayout(self.widget_cardapio_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_cardapio_2 = QPushButton(self.widget_cardapio_2)
        self.btn_cardapio_2.setObjectName(u"btn_cardapio_2")
        self.btn_cardapio_2.setMinimumSize(QSize(181, 161))
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
        self.btn_cardapio_2.setPalette(palette)
        self.btn_cardapio_2.setStyleSheet(u"background-color: #adc178; \n"
"image: url(:/icon/entrada 1.png);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout_6.addWidget(self.btn_cardapio_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_13 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)

        self.lbl_cardapio_2 = QLabel(self.widget_cardapio_2)
        self.lbl_cardapio_2.setObjectName(u"lbl_cardapio_2")
        self.lbl_cardapio_2.setStyleSheet(u"background-color: #588157; \n"
"font: 87 8pt \"Arial Black\";\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.lbl_cardapio_2)

        self.horizontalSpacer_14 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_14)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_14.addWidget(self.widget_cardapio_2)

        self.widget_status_2 = QWidget(self.central_widget)
        self.widget_status_2.setObjectName(u"widget_status_2")
        self.verticalLayout_7 = QVBoxLayout(self.widget_status_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_status_2 = QPushButton(self.widget_status_2)
        self.btn_status_2.setObjectName(u"btn_status_2")
        self.btn_status_2.setMinimumSize(QSize(181, 161))
        self.btn_status_2.setStyleSheet(u"background-color: #adc178; \n"
"image: url(:/icon/prato.png);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout_7.addWidget(self.btn_status_2)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_15 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_15)

        self.lbl_status_2 = QLabel(self.widget_status_2)
        self.lbl_status_2.setObjectName(u"lbl_status_2")
        self.lbl_status_2.setStyleSheet(u"background-color: #588157; \n"
"font: 87 8pt \"Arial Black\";\n"
"")

        self.horizontalLayout_15.addWidget(self.lbl_status_2)

        self.horizontalSpacer_16 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_16)


        self.verticalLayout_7.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_14.addWidget(self.widget_status_2)

        self.widget_pagamento_2 = QWidget(self.central_widget)
        self.widget_pagamento_2.setObjectName(u"widget_pagamento_2")
        self.verticalLayout_8 = QVBoxLayout(self.widget_pagamento_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_pagamento_2 = QPushButton(self.widget_pagamento_2)
        self.btn_pagamento_2.setObjectName(u"btn_pagamento_2")
        self.btn_pagamento_2.setMinimumSize(QSize(181, 161))
        self.btn_pagamento_2.setStyleSheet(u"background-color: #adc178; \n"
"image: url(:/icon/bebida.png);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout_8.addWidget(self.btn_pagamento_2)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_17 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_17)

        self.label_pagamento_2 = QLabel(self.widget_pagamento_2)
        self.label_pagamento_2.setObjectName(u"label_pagamento_2")
        self.label_pagamento_2.setStyleSheet(u"background-color: #588157	; \n"
"font: 87 8pt \"Arial Black\";")

        self.horizontalLayout_16.addWidget(self.label_pagamento_2)

        self.horizontalSpacer_18 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_18)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_14.addWidget(self.widget_pagamento_2)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.btn_voltar_menu_principal = QPushButton(self.central_widget)
        self.btn_voltar_menu_principal.setObjectName(u"btn_voltar_menu_principal")
        self.btn_voltar_menu_principal.setStyleSheet(u"background-color: #adc178; \n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;\n"
"")

        self.verticalLayout.addWidget(self.btn_voltar_menu_principal)

        self.verticalSpacer_6 = QSpacerItem(18, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.widget_opcao_3.raise_()
        self.linha_2.raise_()
        self.btn_voltar_menu_principal.raise_()

        self.horizontalLayout.addWidget(self.central_widget)


        self.retranslateUi(Dialog_cardapio)

        QMetaObject.connectSlotsByName(Dialog_cardapio)
    # setupUi

    def retranslateUi(self, Dialog_cardapio):
        Dialog_cardapio.setWindowTitle(QCoreApplication.translate("Dialog_cardapio", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.widget_7.setToolTip(QCoreApplication.translate("Dialog_cardapio", u"<html><head/><body><p><img src=\":/icon/restaurant.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_cardapio_2.setToolTip(QCoreApplication.translate("Dialog_cardapio", u"<html><head/><body><p><span style=\" font-size:16pt; color:#aa0000;\">CARD\u00c1PIO</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cardapio_2.setText("")
        self.lbl_cardapio_2.setText(QCoreApplication.translate("Dialog_cardapio", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#005500;\">ENTRADAS</span></p></body></html>", None))
        self.btn_status_2.setText("")
        self.lbl_status_2.setText(QCoreApplication.translate("Dialog_cardapio", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#005500;\">PRATOS</span></p></body></html>", None))
        self.btn_pagamento_2.setText("")
        self.label_pagamento_2.setText(QCoreApplication.translate("Dialog_cardapio", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#005500;\">BEBIDAS</span></p></body></html>", None))
        self.btn_voltar_menu_principal.setText(QCoreApplication.translate("Dialog_cardapio", u"Voltar para Menu Principal", None))
    # retranslateUi

