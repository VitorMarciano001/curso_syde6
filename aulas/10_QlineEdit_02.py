from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QLineEdit
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit")

        self.line1 = QLineEdit()
        self.line1.setMaxLength(5)
        self.line1.setPlaceholderText("Digite sua senha")
        #self.line1.setInputMask("00/00/0000;_")

        layout = QVBoxLayout()
        layout.addWidget(self.line1)

        

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.line1.editingFinished.connect(self.editing_finished)
        self.line1.returnPressed.connect(self.return_pressed)
        self.line1.textChanged.connect(self.text_changed)
        self.line1.selectionChanged.connect(self.selection_changed)
        self.line1.textEdited.connect(self.text_edited)


    def editing_finished(self):
        print('terminou a edição')
    
    def return_pressed(self):
        print('return pressed')
        self.centralWidget().setText(f'Texto digitado: {self.line1.text()}')
        
    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())
            
    def text_changed(self, s):
        print("Texto alterado...")
        print(s)
        
    def text_edited(self, s):
        print("Texto editado..")
        print(s)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()