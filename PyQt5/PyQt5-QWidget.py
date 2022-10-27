import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("QWindow")
        self.setWindowIcon(QIcon('python.png'))

        self.setFixedHeight(400)
        self.setFixedWidth(400)
        self.setStyleSheet('background-color:green')
        
app = QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())

