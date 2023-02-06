import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #---------------------------------------------------------
        # Dando nome a janela e definindo seu tamanho
        self.setWindowTitle("Organizador de arquivos")
        self.setMinimumSize(580,340)
        self.setMaximumSize(680,440)
        #---------------------------------------------------------

        #---------------------------------------------------------
        # Frame principal
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background: #ffb347")
        self.main_layout = QVBoxLayout(self.central_frame)  
        self.main_layout.setContentsMargins(0,0,0,0)
        #self.main_layout.setSpacing(0)
        #---------------------------------------------------------      
        
        #---------------------------------------------------------
        # Frame de cima onde ficarao a label com icon
        self.top_frame = QFrame()
        self.top_frame_layout = QVBoxLayout(self.top_frame)
        self.top_frame_layout.setContentsMargins(0,20,0,0)
        #---------------------------------------------------------

        #---------------------------------------------------------
        # Frame do meio onde ficarao o line edit e botao
        self.mid_frame = QFrame()
        self.mid_frame_layout = QHBoxLayout(self.mid_frame)
        #---------------------------------------------------------

        #---------------------------------------------------------
        # Frame de baixo onde ficara o botao de organizar
        self.bot_frame = QFrame()
        self.bot_frame_layout = QHBoxLayout(self.bot_frame)
        #---------------------------------------------------------

        #---------------------------------------------------------
        # Configurando a barra de creditos
        self.credit_bar = QFrame()
        self.credit_bar.setStyleSheet("background: #efa2c8")
        self.credit_bar.setMinimumHeight(25)
        self.credit_bar.setMaximumHeight(25)
        self.credit_bar_layout = QHBoxLayout(self.credit_bar)
        self.credit_bar_layout.setContentsMargins(10,2.5,10,2.5)
        self.credit_bar_layout.setSpacing(0)
        #---------------------------------------------------------

        #//////////////////////////////////////////////////////////
        # INICIANDO TODOS OS WIDGETS EM USO NA APLICACAO
        #---------------------------------------------------------
        # Label que recebera a imagem
        self.lbl_icon = QLabel("Teste")
        self.lbl_icon.setPixmap(QPixmap("icons/folder.png"))
        self.lbl_icon.setAlignment(Qt.AlignHCenter)
        #---------------------------------------------------------
        # Label de cima que tera um icone
        self.lbl_text = QLabel("Seu organizador")
        self.lbl_text.setAlignment(Qt.AlignHCenter)
        #---------------------------------------------------------

        #---------------------------------------------------------
        # LineEdit onde aparecera o caminho da pasta
        self.line_select_folder = QLineEdit()
        self.line_select_folder.setAlignment(Qt.AlignHCenter)
        self.line_select_folder.setPlaceholderText("Caminho da Pasta")
        self.line_select_folder.setMinimumWidth(350)
        self.line_select_folder.setMaximumWidth(350)
        self.line_select_folder.setMinimumHeight(30)
        self.line_select_folder.setMaximumHeight(30)
        #---------------------------------------------------------

        #---------------------------------------------------------
        # Espacadores do frame do meio
        self.spacer_mid_left = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.spacer_mid_right = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        #---------------------------------------------------------

        #---------------------------------------------------------
        # Botao que ira procurar arquivo
        self.btn_search = QPushButton("Select")
        self.btn_search.setStyleSheet("background: #ff6961")
        self.btn_search.setMinimumWidth(100)
        self.btn_search.setMaximumWidth(100)
        self.btn_search.setMinimumHeight(30)
        self.btn_search.setMaximumHeight(30)
        #---------------------------------------------------------

        #---------------------------------------------------------
        # Botao qe fara a organizacao do arquivo
        self.btn_organize = QPushButton("Organizar")
        self.btn_organize.setStyleSheet("background: #ff6961")
        self.btn_organize.setMinimumWidth(110)
        self.btn_organize.setMaximumWidth(110)
        self.btn_organize.setMinimumHeight(35)
        self.btn_organize.setMaximumHeight(35)
        #---------------------------------------------------------

        #---------------------------------------------------------
        self.lbl_name = QLabel("Created by: Vitor Marciano")
        self.spacer_credit_bar = QSpacerItem(10,10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.lbl_date = QLabel("@2023")
        #---------------------------------------------------------
        #//////////////////////////////////////////////////////////


        #//////////////////////////////////////////////////////////
        # INSERCOES DE WIDGETS E ITENS AOS LAYOUTS CORRETOS
        #---------------------------------------------------------
        # Adicionando os frames ao frame central
        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.mid_frame)
        self.main_layout.addWidget(self.bot_frame)
        self.main_layout.addWidget(self.credit_bar)
        #---------------------------------------------------------

        #---------------------------------------------------------
        # Adicionando elementos ao top, mid e bot frames
        self.top_frame_layout.addWidget(self.lbl_icon)
        self.top_frame_layout.addWidget(self.lbl_text)
        self.mid_frame_layout.addItem(self.spacer_mid_left)
        self.mid_frame_layout.addWidget(self.line_select_folder)
        self.mid_frame_layout.addWidget(self.btn_search)
        self.mid_frame_layout.addItem(self.spacer_mid_right)
        self.bot_frame_layout.addWidget(self.btn_organize)
        #---------------------------------------------------------

        #---------------------------------------------------------
        # Adicionando texto ao credit bar
        self.credit_bar_layout.addWidget(self.lbl_name)
        self.credit_bar_layout.addItem(self.spacer_credit_bar)
        self.credit_bar_layout.addWidget(self.lbl_date)
        #---------------------------------------------------------
        #//////////////////////////////////////////////////////////

        self.setCentralWidget(self.central_frame)

if (__name__ == "__main__"):
    app =QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()