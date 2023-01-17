from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QSpinBox
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QSpinBox')

        self.sp = QSpinBox()
        self.sp.setMinimum(0)
        self.sp.setMaximum(60)
        self.sp.setPrefix("R$: ")
        self.sp.setSuffix(' Final')
        #self.sp.setSingleStep(3)

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