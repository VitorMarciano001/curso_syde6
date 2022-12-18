from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minha janela")
        self.setFixedSize(QSize(600,400))

        button = QPushButton("Botao Principal")
        self.setCentralWidget(button)

        button.setCheckable(True)
        button.clicked.connect(self.imprimir)
        button.clicked.connect(self.clicado)

    def imprimir(self):
        print("Botao clicado")

    def clicado(self, s):
        print("clicado", s)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()