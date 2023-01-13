import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CheckBox")
        self.setMaximumSize(600,520)
        self.setMinimumSize(300,220)

        self.lbl = QLabel("Voce fuma?")
        self.check = QCheckBox("Sim")
        self.check.setTristate(True)
        self.lbl2 = QLabel()
        #self.check.setCheckState(Qt.Checked)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.check)
        layout.addWidget(self.lbl2)

        container = QWidget()
        container.setLayout(layout)

        
        self.setCentralWidget(container)

        self.check.stateChanged.connect(self.state)

    def state(self, s):
        print(s)
        if s == 2:
            self.lbl2.setText("Preencha o formulario")
        else:
            self.lbl2.setText("")


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()