from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minha janela")
        self.setFixedSize(QSize(600,400))

        self.button = QPushButton("Botao Principal")
        self.setCentralWidget(self.button)

        self.button.setCheckable(True)
        self.button.clicked.connect(self.imprimir)
        self.button.clicked.connect(self.clicado)

    def imprimir(self):
        print("Botao clicado")

    def clicado(self, s):
        print("Clicado", s)
        if s:
            self.button.setStyleSheet(u"background-color: green")
            self.button.setText("Ligado")
        else:
            self.button.setStyleSheet(u"background-color: red")
            self.button.setText("Desligado")

        #self.button.setEnabled(False)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()