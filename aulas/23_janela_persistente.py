from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.lbl = QLabel("Sua nova janela")
        self.lbl.setAlignment(Qt.AlignHCenter)

        self.layout.addWidget(self.lbl)

        self.setLayout(self.layout)




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = AnotherWindow()

        self.setWindowTitle("Principal")
        self.setFixedSize(QSize(300,120))

        self.btn = QPushButton("Clique para abrir uma nova janela")
        self.btn.clicked.connect(self.call_window)


        self.setCentralWidget(self.btn)

    def call_window(self):
        self.w.show()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()