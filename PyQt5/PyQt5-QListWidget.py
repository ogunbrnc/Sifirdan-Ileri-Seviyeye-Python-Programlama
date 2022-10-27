import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("QListWidget")
        self.setWindowIcon(QIcon('python.png'))

        self.list_widget = QListWidget(self)
        self.list_widget.insertItem(0,"C")
        self.list_widget.insertItem(1,"C++")
        self.list_widget.insertItem(2,"Python")
        self.list_widget.clicked.connect(self.elemanaTiklandi)
        
    def elemanaTiklandi(self):
        item = self.list_widget.currentItem()
        print(item.text() + " tiklandi")


        
app = QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())