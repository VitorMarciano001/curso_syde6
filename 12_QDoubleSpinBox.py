from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QDoubleSpinBox, QAbstractSpinBox
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QSpinBox')

        self.sp = QDoubleSpinBox()
        self.sp.setMinimum(0)
        self.sp.setMaximum(60)
        self.sp.setPrefix("R$: ")
        #self.sp.setSuffix(' Final')
        #self.sp.setSingleStep(3)
        self.sp.setButtonSymbols(QAbstractSpinBox.NoButtons) # REMOVE OS BOTOES E DEIXA SO UM CAMPO DEVALORES

        layout = QVBoxLayout()
        layout.addWidget(self.sp)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.sp.valueChanged.connect(self.value_c)

    def value_c(self, v):
        print(v)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()