from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout,
    QLineEdit, QLabel, QTableWidget, QTableWidgetItem,
    QPushButton, QFrame
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

        self.btn_print = QPushButton("Imprimir")
        self.tb = QTableWidget()
    
        lista= [
            ['001', 'R$120,00','R$ 38,00','R$ 52,00'],
            ['002', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['003', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['004', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['005', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['006', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['007', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['008', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['009', 'R$100,00','R$ 18,00','R$ 5,00'],
        ]
        self.tb.setRowCount(len(lista))
        self.tb.setColumnCount(len(lista[0]))

        for row, text in enumerate(lista):
            for colum, data in enumerate(text):
                self.tb.setItem(row, colum, QTableWidgetItem(str(data)))

        self.layout.addWidget(self.tb)
        self.layout.addWidget(self.btn_print)

        container = QFrame()
        container.setLayout(self.layout)

        self.setCentralWidget(container)

        self.btn_print.clicked.connect(self.print_table)

    def print_table(self):
        data = []
        table_att = []

        for row in range(self.tb.rowCount()):
            for colum in range(self.tb.columnCount()):
                data.append(self.tb.item(row, colum).text())
            table_att.append(data)
            data = []
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()