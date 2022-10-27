import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("QLabel")
        self.setWindowIcon(QIcon('python.png'))

        label= QLabel(self)
        label.setText("QLabel")
        label.move(100,100)
        label.resize(80,80)
        label.setStyleSheet("border:4px solid red;border-radius:40;")

app = QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())

