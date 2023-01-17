from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QToolBar, QLabel, QStatusBar
from PySide6.QtCore import Qt, QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("QToolBar")

        
        self.lbl = QLabel("QToolBar")
        self.lbl.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)

        toolbar = QToolBar("Minha Toolbar")
        toolbar.setIconSize(QSize(24,24))
        self.addToolBar(toolbar)
        


        btn_action = QAction(QIcon("icons/home.png"),"Botao 1", self)
        btn_action.setStatusTip("Primeiro botao")
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

        btn_Action_2 = QAction("botao 2", self)
        btn_Action_2.setStatusTip("Segundo botao")
        btn_Action_2.triggered.connect(self.funcao)
        btn_Action_2.setCheckable(True)
        toolbar.addAction(btn_Action_2)
        

        container = QFrame()
        container.setLayout(layout)

        self.setStatusBar(QStatusBar(self))

        self.setCentralWidget(container)

    def funcao(self, f):
        print("clicked", f)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()