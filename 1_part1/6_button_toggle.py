from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("The app")
        button = QPushButton("Press")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)
        button.clicked.connect(self.button_toggled)
        self.setFixedSize(QSize(300, 400))
        self.setCentralWidget(button)

    def button_clicked(self):
        print('Clicked')

    def button_toggled(self, checked):
        print("Button state ", checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()