from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QFrame, QVBoxLayout, QLabel
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit")
        self.setFixedSize(QSize(320,300))
        #self.setMinimumSize(320,200)
        #self.setMaximumSize(620,720)

        self.input = QLineEdit()
        self.lbl = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.lbl)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.input.textChanged.connect(self.texte)

    def texte(self):
        self.lbl.setText("Valor mudado")



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

