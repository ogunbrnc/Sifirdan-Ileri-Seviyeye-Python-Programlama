import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("QHBoxLayout&QVBoxLayout")
        self.setWindowIcon(QIcon('python.png'))

        vbox= QVBoxLayout()
        hbox= QHBoxLayout()
        vbox2= QVBoxLayout()

        buton1=QPushButton("buton1")
        buton2=QPushButton("buton2")
        hbox.addWidget(buton1)
        hbox.addWidget(buton2)

        buton3=QPushButton("buton3")
        buton4=QPushButton("buton4")
        vbox2.addWidget(buton3)
        vbox2.addWidget(buton4)


        vbox.addLayout(hbox)
        vbox.addLayout(vbox2)
        self.setLayout(vbox)
      

app = QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())

