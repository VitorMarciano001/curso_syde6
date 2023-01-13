import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QFrame, 
                               QLineEdit, QComboBox, QLabel, 
                               QVBoxLayout)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # SETANDO CONFIGURACOES DA JANELA
        self.setWindowTitle("Busca CEP")
        self.setMaximumSize(600,480)
        self.setMinimumSize(400,320)

        self.lbl1 = QLabel("Nome")
        self.lbl1.setAlignment(Qt.AlignHCenter)
        self.lne1 = QLineEdit()

        self.lbl2 = QLabel("Sexo")
        self.lbl2.setAlignment(Qt.AlignHCenter)
        self.cmb = QComboBox()
        self.cmb.addItems(["Masculino", "Feminino", "Outro"])

        self.lbl3 = QLabel("CEP")
        self.lbl3.setAlignment(Qt.AlignHCenter)
        self.lne3 = QLineEdit()
        

        self.lbl4 = QLabel("Lagradouro")
        self.lbl4.setAlignment(Qt.AlignHCenter)
        self.lne4 = QLineEdit()

        self.lbl5 = QLabel("Bairro")
        self.lbl5.setAlignment(Qt.AlignHCenter)
        self.lne5 = QLineEdit()

        self.lbl6 = QLabel("Cidade")
        self.lbl6.setAlignment(Qt.AlignHCenter)
        self.lne6 = QLineEdit()

        # SETANDO LAYOUT
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lbl1)
        self.layout.addWidget(self.lne1)
        self.layout.addWidget(self.lbl2)
        self.layout.addWidget(self.cmb)
        self.layout.addWidget(self.lbl3)
        self.layout.addWidget(self.lne3)
        self.layout.addWidget(self.lbl4)
        self.layout.addWidget(self.lne4)
        self.layout.addWidget(self.lbl5)
        self.layout.addWidget(self.lne5)
        self.layout.addWidget(self.lbl6)
        self.layout.addWidget(self.lne6)

        # SETANDO QFRAME E ADICIONANDO AO WIDGET CENTRAL
        container = QFrame()
        container.setLayout(self.layout)

        self.setCentralWidget(container)



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()