from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton, QFrame, QVBoxLayout
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculador de metro cubico")
        self.setMaximumSize(600,520)
        self.setMinimumSize(300,400)

        self.lbl_altura = QLabel("Altura")
        self.altura = QLineEdit()
        
        self.lbl_comprimento = QLabel("Comprimento")
        self.comprimento = QLineEdit()
        
        self.lbl_largura = QLabel("Largura")
        self.largura = QLineEdit()

        self.resultado = QLabel()
        self.button = QPushButton("Calcular")
        self.button.setStyleSheet("background-color:red")

        

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_altura)
        layout.addWidget(self.altura)
        layout.addWidget(self.lbl_comprimento)
        layout.addWidget(self.comprimento)
        layout.addWidget(self.lbl_largura)
        layout.addWidget(self.largura)
        layout.addWidget(self.resultado)
        layout.addWidget(self.button)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.button.clicked.connect(self.calcular)

    def calcular(self):
        resultador = str(
            float(self.altura.text())*
            float(self.comprimento.text())*
            float(self.largura.text())
        )
        self.resultado.setText(f"O resultado e: {resultador} metros cubicos")



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()