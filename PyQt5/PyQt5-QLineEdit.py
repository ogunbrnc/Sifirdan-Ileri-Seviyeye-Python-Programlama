import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt5.QtGui import QIcon,QIntValidator

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("QLineEdit")
        self.setWindowIcon(QIcon('python.png'))

        self.line_edit=QLineEdit(self)
        self.line_edit.setGeometry(80,80,150,40)

        #self.line_edit.textChanged.connect(self.print_text)
        self.line_edit.editingFinished.connect(self.print_text)

        #validator
        #self.line_edit.setValidator(QIntValidator())

        #maximum uzunluk
        #self.line_edit.setMaxLength(4)

        #sifreyi gizleme
        #self.line_edit.setEchoMode(QLineEdit.Password)

        #telefon no icin formatlama
        self.line_edit.setInputMask('+99_999_999_999')

    def print_text(self):
        print(self.line_edit.text())

app = QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())
