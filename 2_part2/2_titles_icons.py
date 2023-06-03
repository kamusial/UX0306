from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QMovie, QPixmap
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        # self.setFixedWidth(700)
        # self.setFixedHeight(400)
        self.setWindowIcon(QIcon('../images/java.png'))
        self.setWindowTitle("Tytul")
#        self.setStyleSheet('background-color:green')
#        self.setWindowOpacity(0.9)

        # label = QLabel('Python', self)
        # label.setText("text labelki")
        # label.move(100, 100)
        # label.setFont(QFont("Sanserif", 19))
        # label.setStyleSheet('color:red')

        # label = QLabel(self)
        # movie = QMovie('../images/sky.gif')
        # movie.setSpeed(100)
        # label.setMovie(movie)
        # movie.start()

        label = QLabel(self)
        pixmap = QPixmap('../images/python.png')
        label.setPixmap(pixmap)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())