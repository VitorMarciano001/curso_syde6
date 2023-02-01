import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QIcon
from organizer import Ui_MainWindow
import shutil
import os


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Meu organizador")
        appicon = QIcon("icons/folder.png")
        self.setWindowIcon(appicon)


        self.btn_search.clicked.connect(self.open_path)
        self.btn_organize.clicked.connect(self.organizer)



    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(self, str("Ppasta com arquivo"),
                                                     '/home',
                                                      QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.text_path.setText(self.path)
        self.path = str(self.path)


    def organizer(self):
        path  = self.path
        files = os.listdir(path)
        
        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]
            if os.path.exists(path + '/' + extension):
                shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
            else:
                os.makedirs(path + '/' + extension)
                shutil.move(path + '/' + files, path + '/' + extension)



        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Arquivos organizados com sucesso")
        msg.exec()

if (__name__ == "__main__"):
    app =QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()