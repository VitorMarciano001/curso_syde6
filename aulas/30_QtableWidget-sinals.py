from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout,
    QLineEdit, QLabel, QTableWidget, QTableWidgetItem
)
from PySide6.QtCore import Qt, QSize
import sys

"""def cellActivated (row, column)
   def cellChanged (row, column)
   def cellClicked (row, column)
   def cellDoubleClicked (row, column)
   def cellEntered (row, column)
   def cellPressed (row, column)
   def currentCellChanged (currentRow, currentColumn, previousRow, previousColumn)
   def currentItemChanged (current, previous)
   def itemActivated (item)
   def itemChanged (item)
   def itemClicked (item)
   def itemDoubleClicked (item)
   def itemEntered (item)
   def itemPressed (item)
   def itemSelectionChanged ()
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # DEFININDO NOME E TAMANHO
        self.setWindowTitle("Minha table")
        self.setFixedSize(QSize(600,520))

        self.layout = QVBoxLayout()

        self.tb = QTableWidget()
        self.tb.setRowCount(3)
        self.tb.setColumnCount(3)

        self.tb.setHorizontalHeaderLabels(["Nome","Endereco","E-mail"])
        self.tb.setItem(0,0, QTableWidgetItem("Paula"))
        self.tb.setItem(0,1, QTableWidgetItem("rua das paulas"))
        self.tb.setItem(0,2, QTableWidgetItem("paulinha@gmail.com"))

        self.tb.setItem(1,0, QTableWidgetItem("Vitor"))
        self.tb.setItem(1,1, QTableWidgetItem("Rua dos alfajores"))
        self.tb.setItem(1,2, QTableWidgetItem("nao.interessa@gmail.com"))

        self.layout.addWidget(self.tb)

        self.setCentralWidget(self.tb)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()