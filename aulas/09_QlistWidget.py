from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QFrame, QListWidget, QVBoxLayout)
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ListWidget")
        self.lw = QListWidget()
        self.lw.addItems(['ITEM 01', 'ITEM 02', 'ITEM 03'])

        layout = QVBoxLayout()
        layout.addWidget(self.lw)

        container = QFrame()
        container.setLayout(layout)

        self.lw.itemDoubleClicked.connect(self.abri_janela)
        self.lw.currentItemChanged.connect(self.indice)
        self.lw.currentTextChanged.connect(self.texto_alterado)

        self.setCentralWidget(container)

    def abri_janela(self, i):
        print(i)

    def indice(self, i):
        print(i)

    def texto_alterado(self, t):
        print(t)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()