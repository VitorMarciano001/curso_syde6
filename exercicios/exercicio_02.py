import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QFrame, 
                               QLineEdit, QComboBox, QLabel, 
                               QVBoxLayout)
from PySide6.QtCore import Qt
import pycep_correios

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # SETANDO CONFIGURACOES DA JANELA
        self.setWindowTitle("Busca CEP")
        self.setMaximumSize(600,480)
        self.setMinimumSize(400,320)

        # LABEL E LINE EDIT NOME
        self.lbl_nome = QLabel("Nome")
        self.lbl_nome.setAlignment(Qt.AlignHCenter)
        self.nome = QLineEdit()

        # LABEL E COMBO BOX SEXO
        self.lbl_sexo = QLabel("Sexo")
        self.lbl_sexo.setAlignment(Qt.AlignHCenter)
        self.cmb_sexo = QComboBox()
        self.cmb_sexo.addItems(["Masculino", "Feminino", "Outro"])

        # LABEL E LINE EDIT CEP
        self.lbl_cep = QLabel("CEP")
        self.lbl_cep.setAlignment(Qt.AlignHCenter)
        self.cep = QLineEdit()

        # LABEL E LINE EDIT LOGRADOURO
        self.lbl_lagra = QLabel("Logradouro")
        self.lbl_lagra.setAlignment(Qt.AlignHCenter)
        self.lagradouro = QLineEdit()

        # LABEL E LINE EDIT BAIRRO
        self.lbl_bairro = QLabel("Bairro")
        self.lbl_bairro.setAlignment(Qt.AlignHCenter)
        self.bairro = QLineEdit()

        # LABEL E LINE EDIT CIDADE
        self.lbl_city = QLabel("Cidade")
        self.lbl_city.setAlignment(Qt.AlignHCenter)
        self.cidade = QLineEdit()

        # SETANDO LAYOUT
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lbl_nome)
        self.layout.addWidget(self.nome)
        self.layout.addWidget(self.lbl_sexo)
        self.layout.addWidget(self.cmb_sexo)
        self.layout.addWidget(self.lbl_cep)
        self.layout.addWidget(self.cep)
        self.layout.addWidget(self.lbl_lagra)
        self.layout.addWidget(self.lagradouro)
        self.layout.addWidget(self.lbl_bairro)
        self.layout.addWidget(self.bairro)
        self.layout.addWidget(self.lbl_city)
        self.layout.addWidget(self.cidade)

        # SETANDO QFRAME E ADICIONANDO AO WIDGET CENTRAL
        container = QFrame()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # CONECTANDO O LINE EDIT A FUNCAO BUSCA_CEP PARA MUDAR AS LINE EDIT CORRESPONDENTES
        self.cep.editingFinished.connect(self.busca_cep)

    # FUNCAO QUE BUSCA O CEP E RETORNA NAS DEVIDAS LINE EDIT
    def busca_cep(self):
        endereco = pycep_correios.get_address_from_cep(self.cep.text())
        print(endereco)
        self.lagradouro.setText(endereco['logradouro'])
        self.bairro.setText(endereco['bairro'])
        self.cidade.setText(endereco['cidade'])




app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()