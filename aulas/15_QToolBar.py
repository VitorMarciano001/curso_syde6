from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QToolBar
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("QToolBar")

        self.tb = QToolBar("Menu")

        layout = QVBoxLayout()

        container = QFrame()
        container.setLayout(layout)


        self.setCentralWidget(container)



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()