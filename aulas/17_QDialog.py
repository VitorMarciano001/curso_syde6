import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,QFrame,
                               QDialog, QDialogButtonBox, QVBoxLayout, QLabel)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # DEFININDO NOME E TAMANHO DA JANELA
        self.setWindowTitle("QDialog")
        self.setMinimumSize(300,180)
        self.setMaximumSize(400,280)


        # INICIALIZANDO BOTAO, COLOCANDO COR E CONECTANDO A FUNCAO
        self.btn = QPushButton("Clique para abrir um Dialog")
        self.btn.setStyleSheet(u"background-color:green")
        self.btn.clicked.connect(self.btn_clicked)
        #self.btn.setCheckable(True)


        # ADICIONANDO AO WIDGET CENTRAL
        self.setCentralWidget(self.btn)


    def btn_clicked(self, s):
        print("click", s)
        dlg = Meu_Dialog()
        if dlg.exec_():
            print("sucesso")
        else:
            print("cancelar!")


class Meu_Dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu Dialog")

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.btn_box = QDialogButtonBox(buttons)
        self.btn_box.accepted.connect(self.accept)
        self.btn_box.rejected.connect(self.reject)

        self.btn_box.button(QDialogButtonBox.Ok).setText("Sim")
        self.btn_box.button(QDialogButtonBox.Cancel).setText("Cancelar")

        self.btn_box.addButton("Executar", QDialogButtonBox.ActionRole)
        self.btn_box.clicked.connect(self.executar)

        self.layout = QVBoxLayout()
        msg = QLabel("Voce deseja continuar")
        self.layout.addWidget(msg)
        self.layout.addWidget(self.btn_box)
        self.setLayout(self.layout)

        
    def executar(self):
        print("Executando...")

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()