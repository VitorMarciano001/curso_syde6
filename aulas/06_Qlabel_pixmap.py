import sys
from PySide6.QtWidgets import QApplication,QMainWindow, QWidget, QLabel
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Imagem")
        self.setFixedSize(QSize(400,300))
        
        self.lbl = QLabel()
        self.lbl.setPixmap(QPixmap("img/IMG_20221114_131517008_MFNR.jpg"))
        self.lbl.setScaledContents(True)

        self.setCentralWidget(self.lbl)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()