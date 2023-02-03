# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(767, 465)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_frame = QFrame(self.centralwidget)
        self.left_frame.setObjectName(u"left_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_frame.sizePolicy().hasHeightForWidth())
        self.left_frame.setSizePolicy(sizePolicy)
        self.left_frame.setMinimumSize(QSize(0, 0))
        self.left_frame.setMaximumSize(QSize(0, 16777215))
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logo_frame = QFrame(self.left_frame)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setFrameShape(QFrame.NoFrame)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.logo_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.logo_frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.logo_frame)

        self.btn_frame = QFrame(self.left_frame)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setFrameShape(QFrame.NoFrame)
        self.btn_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.btn_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.toolBox = QToolBox(self.btn_frame)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 101, 289))
        self.verticalLayout_9 = QVBoxLayout(self.page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")

        self.verticalLayout_9.addWidget(self.btn_home)

        self.btn_cadastro = QPushButton(self.page)
        self.btn_cadastro.setObjectName(u"btn_cadastro")

        self.verticalLayout_9.addWidget(self.btn_cadastro)

        self.btn_contatos = QPushButton(self.page)
        self.btn_contatos.setObjectName(u"btn_contatos")

        self.verticalLayout_9.addWidget(self.btn_contatos)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")

        self.verticalLayout_9.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Menu")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 89, 291))
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_8.addWidget(self.label_5)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7)

        self.toolBox.addItem(self.page_2, u"Informations")

        self.verticalLayout_6.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.btn_frame)


        self.horizontalLayout.addWidget(self.left_frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setMaximumSize(QSize(16777215, 16777215))
        self.main_frame.setSizeIncrement(QSize(0, 0))
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.main_frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.top_frame = QFrame(self.main_frame)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.NoFrame)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_left_menu = QPushButton(self.top_frame)
        self.btn_left_menu.setObjectName(u"btn_left_menu")
        self.btn_left_menu.setStyleSheet(u"image: url(:/icons/menu.png);")

        self.horizontalLayout_2.addWidget(self.btn_left_menu, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.mid_frame = QFrame(self.main_frame)
        self.mid_frame.setObjectName(u"mid_frame")
        sizePolicy.setHeightForWidth(self.mid_frame.sizePolicy().hasHeightForWidth())
        self.mid_frame.setSizePolicy(sizePolicy)
        self.mid_frame.setFrameShape(QFrame.NoFrame)
        self.mid_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.mid_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pages = QStackedWidget(self.mid_frame)
        self.pages.setObjectName(u"pages")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy1)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_7 = QVBoxLayout(self.pg_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.pg_home)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.pages.addWidget(self.pg_home)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_10 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_8 = QLabel(self.pg_sobre)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_10.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.label_9 = QLabel(self.pg_sobre)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(515, 0))
        self.label_9.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.pg_sobre)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_17 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_3 = QFrame(self.pg_contatos)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 200))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 20))
        self.label_15.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_15.addWidget(self.label_15, 0, Qt.AlignHCenter)


        self.verticalLayout_17.addWidget(self.frame_3)

        self.Contatos = QFrame(self.pg_contatos)
        self.Contatos.setObjectName(u"Contatos")
        self.Contatos.setFrameShape(QFrame.NoFrame)
        self.Contatos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.Contatos)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_16 = QLabel(self.Contatos)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_16.addWidget(self.label_16)

        self.label_17 = QLabel(self.Contatos)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_16.addWidget(self.label_17)

        self.label_18 = QLabel(self.Contatos)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_16.addWidget(self.label_18)

        self.label_19 = QLabel(self.Contatos)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_16.addWidget(self.label_19)


        self.verticalLayout_17.addWidget(self.Contatos)

        self.pages.addWidget(self.pg_contatos)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_11 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tabWidget = QTabWidget(self.pg_cadastro)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Cadastro = QWidget()
        self.Cadastro.setObjectName(u"Cadastro")
        self.verticalLayout_12 = QVBoxLayout(self.Cadastro)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame = QFrame(self.Cadastro)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 0, 3, 1, 1)

        self.txt_uf = QLineEdit(self.frame)
        self.txt_uf.setObjectName(u"txt_uf")
        self.txt_uf.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_uf, 4, 2, 1, 1)

        self.txt_logradouro = QLineEdit(self.frame)
        self.txt_logradouro.setObjectName(u"txt_logradouro")
        self.txt_logradouro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_logradouro, 2, 0, 1, 6)

        self.txt_municipio = QLineEdit(self.frame)
        self.txt_municipio.setObjectName(u"txt_municipio")
        self.txt_municipio.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_municipio, 4, 0, 1, 2)

        self.txt_complemento = QLineEdit(self.frame)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_complemento, 3, 1, 1, 4)

        self.txt_bairro = QLineEdit(self.frame)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_bairro, 3, 5, 1, 1)

        self.txt_cep = QLineEdit(self.frame)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cep, 4, 3, 1, 3)

        self.txt_num = QLineEdit(self.frame)
        self.txt_num.setObjectName(u"txt_num")
        self.txt_num.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_num, 3, 0, 1, 1)

        self.txt_cnpj = QLineEdit(self.frame)
        self.txt_cnpj.setObjectName(u"txt_cnpj")
        self.txt_cnpj.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cnpj, 1, 0, 1, 2)

        self.txt_nome = QLineEdit(self.frame)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome, 1, 2, 1, 4)

        self.txt_telefone = QLineEdit(self.frame)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_telefone, 5, 0, 1, 2)

        self.txt_email = QLineEdit(self.frame)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_email, 5, 2, 1, 4)


        self.verticalLayout_12.addWidget(self.frame)

        self.btn_cadastrar = QPushButton(self.Cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(200, 30))
        self.btn_cadastrar.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_12.addWidget(self.btn_cadastrar, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.Cadastro, "")
        self.Empresas = QWidget()
        self.Empresas.setObjectName(u"Empresas")
        self.verticalLayout_14 = QVBoxLayout(self.Empresas)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_14 = QLabel(self.Empresas)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_14.addWidget(self.label_14)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(self.Empresas)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_3.addWidget(self.tableWidget)

        self.frame_2 = QFrame(self.Empresas)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.btn_excel = QPushButton(self.frame_2)
        self.btn_excel.setObjectName(u"btn_excel")

        self.verticalLayout_13.addWidget(self.btn_excel)

        self.btn_alterar = QPushButton(self.frame_2)
        self.btn_alterar.setObjectName(u"btn_alterar")

        self.verticalLayout_13.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_2)
        self.btn_excluir.setObjectName(u"btn_excluir")

        self.verticalLayout_13.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.Empresas, "")

        self.verticalLayout_11.addWidget(self.tabWidget)

        self.pages.addWidget(self.pg_cadastro)

        self.verticalLayout_5.addWidget(self.pages)


        self.verticalLayout.addWidget(self.mid_frame)

        self.bot_frame = QFrame(self.main_frame)
        self.bot_frame.setObjectName(u"bot_frame")
        self.bot_frame.setFrameShape(QFrame.NoFrame)
        self.bot_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.bot_frame)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.label_3 = QLabel(self.bot_frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label_10 = QLabel(self.bot_frame)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)


        self.verticalLayout.addWidget(self.bot_frame)


        self.horizontalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cadastro de Empresas", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Informations", None))
        self.btn_left_menu.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"SISTEMA DE CADASTRO", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/Imagem3.png\"/></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Este sistema busca no site da receita federal os dados do CNPJ de uma empresa e cadastra numa tabela</p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/whats.png\"/> (19)991266290</p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/email.png\"/> vitor.marciano001@gmail.com</p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/instagram.png\"/>VitorDev</p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/youtube.png\"/> MarcianoDev</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic; text-decoration: underline;\">Empresa</span></p></body></html>", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_num.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numero", None))
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Cadastro), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic; text-decoration: underline;\">EMPRESAS</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME EMPRESA", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Empresas), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CopyRight: Vitor Marciano", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"@2023", None))
    # retranslateUi

