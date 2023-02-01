# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'organizer.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(576, 423)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 105, 97);\n"
"font: 11pt \"C059\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.text_path = QLineEdit(self.frame)
        self.text_path.setObjectName(u"text_path")
        self.text_path.setMinimumSize(QSize(280, 35))
        self.text_path.setMaximumSize(QSize(280, 35))
        self.text_path.setStyleSheet(u"QLineEdit {\n"
"	\n"
"	background-color: rgb(241, 180, 180);\n"
"	color: rgb(224, 27, 36);\n"
"	border: 4px solid #1e90ff;\n"
"	border-radius: 8px;\n"
"}")
        self.text_path.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.text_path)

        self.btn_search = QPushButton(self.frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(100, 35))
        self.btn_search.setMaximumSize(QSize(100, 35))
        font = QFont()
        font.setFamilies([u"C059"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.btn_search.setFont(font)
        self.btn_search.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(241, 180, 180);\n"
"	color: rgb(224, 27, 36);\n"
"	border: 4px solid #1e90ff;\n"
"	border-radius: 8px;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_search)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame)

        self.btn_organize = QPushButton(self.frame_2)
        self.btn_organize.setObjectName(u"btn_organize")
        self.btn_organize.setMinimumSize(QSize(120, 40))
        self.btn_organize.setMaximumSize(QSize(120, 40))
        self.btn_organize.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(241, 180, 180);\n"
"	color: rgb(224, 27, 36);\n"
"	border: 4px solid #1e90ff;\n"
"	border-radius: 8px;\n"
"}")

        self.verticalLayout.addWidget(self.btn_organize, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/folder.png\"/></p><p align=\"center\"><span style=\" font-size:14pt;\">Meu Organizador de arquivos</span></p></body></html>", None))
        self.text_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seu arquivo aqui", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btn_organize.setText(QCoreApplication.translate("MainWindow", u"Organize", None))
    # retranslateUi

