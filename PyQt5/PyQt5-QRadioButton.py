import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("QRadioButton")
        self.setWindowIcon(QIcon('python.png'))

        hbox= QHBoxLayout()
        radio_button1=QRadioButton("C")
        radio_button1.setChecked(True)
        radio_button1.toggled.connect(self.secimYapildi)

        radio_button2=QRadioButton("C++")
        radio_button2.toggled.connect(self.secimYapildi)

        radio_button3=QRadioButton("Python")
        radio_button3.toggled.connect(self.secimYapildi)

        hbox.addWidget(radio_button1)
        hbox.addWidget(radio_button2)
        hbox.addWidget(radio_button3)
        self.setLayout(hbox)
    def secimYapildi(self):
        radio_button=self.sender()
        if radio_button.isChecked():
            print(radio_button.text() + " secildi")
        else:
            print(radio_button.text() + " secimi kaldirildi")

app = QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())

