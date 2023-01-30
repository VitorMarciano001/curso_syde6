from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6 import QtCore
import sys


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        
    def rowCount(self, index):
        return len(self._data)
    
    def columnCount(self, index):
        return len(self._data[0])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("QTableView")
        self.setFixedSize(QSize(500,500))

        self.view = QTableView()

        data= [
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


        self.model = TableModel(data)
        self.view.setModel(self.model)
        self.setCentralWidget(self.view)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()