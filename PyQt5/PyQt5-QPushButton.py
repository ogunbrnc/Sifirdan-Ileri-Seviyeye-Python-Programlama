import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon,QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,800,800)
        self.setWindowTitle("QPushButton")
        self.setWindowIcon(QIcon('python.png'))

        buton=QPushButton(self)
        buton.setText("Tikla")
        #buton.move(200,200)
        buton.setGeometry(20,20,200,200)
        buton.setIcon(QIcon("python.png"))
        buton.setIconSize(QSize(60,60))
        buton.setFont(QFont("Sanserif",14))
        buton.setStyleSheet('background-color:red; color:white')
        buton.clicked.connect(self.butonaTiklandi)

        buton2=QPushButton(self)
        buton2.setText("Tikla")
        #buton.move(200,200)
        buton2.setGeometry(300,300,200,200)
        buton2.setIcon(QIcon("python.png"))
        buton2.setIconSize(QSize(60,60))
        buton2.setFont(QFont("Sanserif",14))
        buton2.setStyleSheet('background-color:blue; color:white')
        buton2.clicked.connect(self.butonaTiklandiIki)

    def butonaTiklandi(self):
        print("Butona tiklandi.")
        
    def butonaTiklandiIki(self):
        print("Butona tiklandi iki.")

app = QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())

