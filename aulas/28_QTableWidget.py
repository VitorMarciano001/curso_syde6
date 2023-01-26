from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout,
    QLineEdit, QLabel, QTableWidget, QTableWidgetItem
)
from PySide6.QtCore import Qt, QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        # DEFININDO NOME E TAMANHO
        self.setWindowTitle("Minha table")
        self.setFixedSize(QSize(600,520))

        self.layout = QVBoxLayout()

        self.tb = QTableWidget()
        self.tb.setRowCount(3)
        self.tb.setColumnCount(3)

        self.tb.setItem(0,0, QTableWidgetItem("Nome"))
        self.tb.setItem(0,1, QTableWidgetItem("Endereco"))
        self.tb.setItem(0,2, QTableWidgetItem("E-mail"))

        self.tb.setItem(1,0, QTableWidgetItem("Vitor"))
        self.tb.setItem(1,1, QTableWidgetItem("Rua dos alfajores"))
        self.tb.setItem(1,2, QTableWidgetItem("nao.interessa@gmail.com"))


        self.layout.addWidget(self.tb)

        self.setCentralWidget(self.tb)






app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()