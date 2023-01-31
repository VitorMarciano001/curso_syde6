# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meu_login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 350)
        MainWindow.setMinimumSize(QSize(300, 350))
        MainWindow.setMaximumSize(QSize(300, 350))
        MainWindow.setStyleSheet(u"background-color: rgb(61, 56, 70);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_login = QLabel(self.frame_2)
        self.lbl_login.setObjectName(u"lbl_login")
        self.lbl_login.setStyleSheet(u"font: 300 italic 20pt \"Fira Sans Condensed\";")

        self.verticalLayout_2.addWidget(self.lbl_login, 0, Qt.AlignHCenter)

        self.line_login = QLineEdit(self.frame_2)
        self.line_login.setObjectName(u"line_login")
        self.line_login.setMaximumSize(QSize(200, 25))
        self.line_login.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(48, 15, 56);\n"
"	color: rgb(199, 48, 48);\n"
"	border: 3px solid #c73030;\n"
"	border-radius: 8px ;\n"
"}")
        self.line_login.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.line_login, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_senha = QLabel(self.frame)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setStyleSheet(u"font: 300 italic 20pt \"Fira Sans Condensed\";")

        self.verticalLayout.addWidget(self.lbl_senha, 0, Qt.AlignHCenter)

        self.line_senha = QLineEdit(self.frame)
        self.line_senha.setObjectName(u"line_senha")
        self.line_senha.setMaximumSize(QSize(200, 25))
        self.line_senha.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(48, 15, 56);\n"
"	color: rgb(199, 48, 48);\n"
"	border: 3px solid #c73030;\n"
"	border-radius: 8px ;\n"
"}")
        self.line_senha.setEchoMode(QLineEdit.Password)
        self.line_senha.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.line_senha, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame)

        self.btn_login = QPushButton(self.frame_3)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setMinimumSize(QSize(120, 30))
        self.btn_login.setMaximumSize(QSize(150, 30))
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(48, 15, 56);\n"
"	color: rgb(199, 48, 48);\n"
"	border: 3px solid #c73030;\n"
"	border-radius: 8px ;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(136, 20, 185);\n"
"	color: rgb(199, 48, 48);\n"
"	border: 3px solid #c73030;\n"
"	border-radius: 8px ;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"	\n"
"	background-color: rgb(71, 6, 88);\n"
"	color: rgb(199, 48, 48);\n"
"	border: 3px solid #c73030;\n"
"	border-radius: 8px ;\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_login, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.line_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira seu Login", None))
        self.lbl_senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.line_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira sua senha", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

