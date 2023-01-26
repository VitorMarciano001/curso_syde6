import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStyle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Icones")
        self.setFixedSize(QSize(600,400))

        icon = QIcon('Temas_Estilos/money.png')
        
        self.btn = QPushButton(icon,"")
        self.btn.setIconSize(QSize(50,50))
        self.setCentralWidget(self.btn)

        self.btn.clicked.connect(self.click)
        
    def click(self, c):
        print("Clicou")

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()