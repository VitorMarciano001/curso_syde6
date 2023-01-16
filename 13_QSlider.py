from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QSlider, QVBoxLayout
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSlider")

        self.slider = QSlider(Qt.Horizontal, self)
        #self.slider.minimum(-10)
        #self.slider.maximum(10)
        self.slider.setRange(-10, 10)
        
        self.slider.valueChanged.connect(self.value_changed)
        self.slider.sliderMoved.connect(self.slider_position)
        self.slider.sliderPressed.connect(self.slider_pressed)
        self.slider.sliderReleased.connect(self.slider_released)



        layout = QVBoxLayout()
        layout.addWidget(self.slider)


        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)


    def value_changed(self, v):
        print(v)

    def slider_position(self, s):
        print(s)

    def slider_pressed(self):
        print("Pressionado")

    def slider_released(self):
        print("Solto")


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()