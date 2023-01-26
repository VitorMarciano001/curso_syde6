import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout,QTableWidgetItem,
                               QPushButton, QLineEdit, QTableWidget)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Tabelas")
        self.setFixedSize(QSize(600,400))
        
        layout = QVBoxLayout()

        self.tb = QTableWidget()
        self.tb.setRowCount(3)
        self.tb.setColumnCount(3)
        
        self.tb.setItem(0,0,QTableWidgetItem("Nome"))
        self.tb.setItem(0,1,QTableWidgetItem("Endereço"))
        self.tb.setItem(0,2,QTableWidgetItem("Email"))
        
        self.tb.setItem(1,0,QTableWidgetItem("Fulano"))
        self.tb.setItem(1,1,QTableWidgetItem("rua x"))
        self.tb.setItem(1,2,QTableWidgetItem("fulano@mail.com"))
        
        
        layout.addWidget(self.tb)

        self.setLayout(layout)
 
        

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()