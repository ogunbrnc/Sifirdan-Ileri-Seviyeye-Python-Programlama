import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("QComboBox")
        self.setWindowIcon(QIcon('python.png'))

        self.combobox=QComboBox(self)
        self.combobox.setGeometry(80,80,150,50)
        self.combobox.addItem("C")
        self.combobox.addItem("C++")
        self.combobox.addItem("Python")
        self.combobox.currentIndexChanged.connect(self.secimDegisti)
    def secimDegisti(self):
        item=self.combobox.currentText()
        print(item)

app = QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())

