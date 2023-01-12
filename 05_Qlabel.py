import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Qlabel")
        self.setFixedSize(QSize(300,280))
        self.lbl = QLabel("Meu programa")
        font = self.lbl.font()
        font.setPointSize(25)
        self.lbl.setFont(font)
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(self.lbl)



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()