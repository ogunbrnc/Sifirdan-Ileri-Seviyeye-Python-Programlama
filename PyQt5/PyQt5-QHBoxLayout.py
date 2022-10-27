import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("QHBoxLayout")
        self.setWindowIcon(QIcon('python.png'))

        hbox=QHBoxLayout()
        buton1=QPushButton("Buton-1")
        buton2=QPushButton("Buton-2")
        buton3=QPushButton("Buton-3")
        hbox.addWidget(buton1)
        hbox.addWidget(buton2)
        hbox.addWidget(buton3)

        self.setLayout(hbox)

app = QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())

