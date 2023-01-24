from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MessageBox")
        self.setFixedSize(QSize(400,320))

        self.button = QPushButton("Show")
        self.setCentralWidget(self.button)

        self.button.setCheckable(True)
        self.button.clicked.connect(self.show_question)

    def show_question(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Question)
        self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.msg.setText("Deseja continuar?")
        resposta = self.msg.exec()
        if resposta == QMessageBox.Yes:
            print("Voce aceitou")
        else:
            print("Voce recusou")

    def show_message(self, s):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setWindowTitle("Message")
        self.msg.setText("Operacao concluida com sucesso")
        self.msg.exec()

        """_
        QMessageBox.NoIcon
        QMessageBox.Question 
        QMessageBox.Information 
        QMessageBox.Warning 
        QMessageBox.Critical
        """



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()