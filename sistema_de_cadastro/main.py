import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6 import QtCore
from qt_material import apply_stylesheet
from cadastro import Ui_MainWindow

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

        #--------------------------------------------------------------------------------
        # Animando left bar
        self.btn_left_menu.clicked.connect(self.animation)
        #--------------------------------------------------------------------------------


    def animation(self):
        width = self.left_frame.width()
        
        newWidth = 0
        if width == 0:
            newWidth = 200
        else:
            newWidth = 0

        self.animation = QPropertyAnimation(self.left_frame, b'minimumWidth')
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setDuration(800)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    apply_stylesheet(app, 'dark_teal.xml')
    window = MainWindow()
    window.show()
    app.exec()