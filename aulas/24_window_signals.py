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

        self.txt = QLineEdit()
        self.txt.textChanged.connect(self.w.lbl.setText) # Sem os parenteses no setText ele nao exige argumento

        self.btn = QPushButton("Clique para escrever")
        self.btn.clicked.connect(self.call_window)


        layout = QVBoxLayout()
        layout.addWidget(self.txt)
        layout.addWidget(self.btn)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


    def call_window(self):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()