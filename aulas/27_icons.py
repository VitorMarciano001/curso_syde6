from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu programa")
        self.setFixedSize(QSize(320, 120))

        icone = self.style().standardIcon(QStyle.SP_DirClosedIcon)

        self.btn = QPushButton(icone, "Clica aqui, porra!!!")
        self.setCentralWidget(self.btn)
        self.btn.setStyleSheet("background-color: purple")
        




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()