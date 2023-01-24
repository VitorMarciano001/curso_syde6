from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QLabel, QStatusBar
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu")
        
        self.lbl = QLabel("QToolBAR")
        self.lbl.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.lbl)
        
        toolbar = QToolBar("Minha toolbar")
        toolbar.setIconSize(QSize(24,24))
        self.addToolBar(toolbar)
        

        btn_action = QAction(QIcon('icons/home.png'),"meu botão", self)
        btn_action.setStatusTip("Este é o seu botão")
        btn_action.triggered.connect(self.funcao)
        btn_action.setCheckable(True)        
        toolbar.addAction(btn_action)
        
        toolbar.addSeparator()
        toolbar.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        
        #Qt.ToolButtonIconOnly - sem texto somente icone
        #Qt.ToolButtonTextOnly - somente texto sem icone
        #Qt.ToolButtonTextBesideIcon icone com o texto acima
        #Qt.ToolButtonTextUnderIcon icone e texto, com texto abaixo
        #Qt.ToolButtonFollowStyle  segue o padrão do descktop
                    
        
        btn_action2 = QAction(QIcon('icons/home.png'),"segundo botão", self)
        btn_action2.setStatusTip("Este éo segundo botão")
        btn_action2.triggered.connect(self.funcao)
        btn_action2.setCheckable(True)        
        toolbar.addAction(btn_action2)
        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()
        menu_arquivo = menu.addMenu("Arquivo")
        menu_arquivo.addAction(btn_action)
        menu_arquivo.addSeparator()
        menu_arquivo.addAction(btn_action2)

        submenu = menu_arquivo.addMenu("Submenu") 
        submenu.addAction(btn_action2)

        
    def funcao(self,s):
        print("click", s)



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()