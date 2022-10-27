import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QHBoxLayout
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("QCheckBox")
        self.setWindowIcon(QIcon('python.png'))

        hbox=QHBoxLayout()
        checkbox_1=QCheckBox("C")
        checkbox_1.stateChanged.connect(self.secimDegisti)
        checkbox_2=QCheckBox("C++")
        checkbox_2.stateChanged.connect(self.secimDegisti)
        checkbox_3=QCheckBox("Python")
        checkbox_3.stateChanged.connect(self.secimDegisti)

        hbox.addWidget(checkbox_1)
        hbox.addWidget(checkbox_2)
        hbox.addWidget(checkbox_3)

        self.setLayout(hbox)
    def secimDegisti(self):
        checkbox=self.sender()
        if checkbox.isChecked():
            print(checkbox.text()+ " secildi")
        else:
            print(checkbox.text()+ " secimi kaldirildi")

app = QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())

