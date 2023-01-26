import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStyle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Meu primeiro programa")
        self.setFixedSize(QSize(600,400))

        icone = self.style().standardIcon(QStyle.SP_DialogSaveButton)
        
        button = QPushButton(icone,"Clique aqui!")
        self.setCentralWidget(button)
        


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()