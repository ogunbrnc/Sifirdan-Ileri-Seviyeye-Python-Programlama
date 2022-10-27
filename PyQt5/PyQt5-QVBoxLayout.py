import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("QVBoxLayout")
        self.setWindowIcon(QIcon('python.png'))

        vbox=QVBoxLayout()
        buton1=QPushButton("Buton-1")
        buton2=QPushButton("Buton-2")
        buton3=QPushButton("Buton-3")

        vbox.addWidget(buton1)
        vbox.addWidget(buton2)
        vbox.addWidget(buton3)
        
        self.setLayout(vbox)


app = QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())

