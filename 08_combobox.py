import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QComboBox, QVBoxLayout
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ComboBox")

        self.cb = QComboBox()
        self.cb.addItems(["Item-01", "Item-02", "Item-03", "Item-04"])
        self.cb.currentIndexChanged.connect(self.mudanca_index)
        self.cb.currentTextChanged.connect(self.mudanca_texto)
        self.cb.setMaxCount(5)
        self.cb.setEditable(True)

        
        self.setCentralWidget(self.cb)

    def mudanca_index(self, i):
        print(i)

    def mudanca_texto(self, t):
        print(t)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
