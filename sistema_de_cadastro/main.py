import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6 import *
from qt_material import apply_stylesheet
from cadastro import Ui_MainWindow
from functions import consulta_cnpj

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cadastro de Empresas")
        self.setFixedSize(QSize(980,520))

        #--------------------------------------------------------------------------------
        # Fazendo coneccoes das paginas
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_cadastro.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_cadastro))
        self.btn_contatos.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_contatos))
        self.btn_sobre.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_sobre))
        #--------------------------------------------------------------------------------

        self.txt_cnpj.editingFinished.connect(self.consulta_api)

        #--------------------------------------------------------------------------------
        # Animando left bar
        self.btn_left_menu.clicked.connect(self.animation)
        #--------------------------------------------------------------------------------


    def animation(self):
        width = self.left_frame.width()
        
        newWidth = 200
        if width == 0:
            newWidth = 200

        self.animation = QPropertyAnimation(self.left_frame, b'maximumWidth')
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setDuration(800)
        self.animation.start()

    def consulta_api(self):
        campo = consulta_cnpj(self.txt_cnpj.text())

        self.txt_nome.setText(campo[0])
        self.txt_logradouro.setText(campo[1])
        self.txt_num.setText(campo[2])
        self.txt_bairro.setText(campo[3])
        self.txt_municipio.setText(campo[4])
        self.txt_uf.setText(campo[5])
        self.txt_cep.setText(campo[6])
        self.txt_telefone.setText(campo[7])
        self.txt_email.setText(campo[8])


if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    apply_stylesheet(app, 'dark_teal.xml')
    window = MainWindow()
    window.show()
    app.exec()