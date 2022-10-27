import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("QGridLayout")
        self.setWindowIcon(QIcon('python.png'))

        grid= QGridLayout()
        buton1=QPushButton("buton-1")
        buton2=QPushButton("buton-2")
        buton3=QPushButton("buton-3")
        buton4=QPushButton("buton-4")
        buton5=QPushButton("buton-5")
        buton6=QPushButton("buton-6")

        grid.addWidget(buton1,0,0)
        grid.addWidget(buton2,0,1)
        grid.addWidget(buton3,0,2)
        grid.addWidget(buton4,1,0)
        grid.addWidget(buton5,1,1)
        grid.addWidget(buton6,1,2)

        self.setLayout(grid)


app = QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())

