import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("QMessageBox")
        self.setWindowIcon(QIcon('python.png'))

        hbox=QHBoxLayout()
        buton1=QPushButton("Uyari")
        buton1.clicked.connect(self.uyariTiklandi)

        buton2=QPushButton("Bilgilendirme")
        buton2.clicked.connect(self.bilgilendirmeTiklandi)

        buton3=QPushButton("Secim")
        buton3.clicked.connect(self.secimTiklandi)

        hbox.addWidget(buton1)
        hbox.addWidget(buton2)
        hbox.addWidget(buton3)
        self.setLayout(hbox)
    
    def uyariTiklandi(self):
        QMessageBox.warning(self,"Uyari", "Bu bir uyari metnidir.")
    def bilgilendirmeTiklandi(self):
        QMessageBox.information(self,"Bilgilendirme","Bu bir bilgilendirme metnidir.")
    def secimTiklandi(self):
        yanit=QMessageBox.question(self, "Secim", "Bu bir secim metnidir", QMessageBox.Yes, QMessageBox.No)
        if yanit == QMessageBox.Yes:
            print("Yes tiklandi")
        else:
            print("No tiklandi")
            
app = QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())
