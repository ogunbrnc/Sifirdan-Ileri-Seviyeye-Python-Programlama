import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,800,800)
        self.setWindowTitle("QTableWidget")
        self.setWindowIcon(QIcon('python.png'))

        table_widget = QTableWidget(self)
        table_widget.setGeometry(100,100,600,400)
        table_widget.setRowCount(3)
        table_widget.setColumnCount(3)

        #Baslik
        table_widget.setItem(0,0,QTableWidgetItem("Ad"))
        table_widget.setItem(0,1,QTableWidgetItem("Soyad"))
        table_widget.setItem(0,2,QTableWidgetItem("Puan"))

        #Veriler.
        table_widget.setItem(1,0,QTableWidgetItem("Ogun"))
        table_widget.setItem(1,1,QTableWidgetItem("Birinci"))
        table_widget.setItem(1,2,QTableWidgetItem("100"))

        table_widget.setItem(2,0,QTableWidgetItem("Yeliz"))
        table_widget.setItem(2,1,QTableWidgetItem("Akkaya"))
        table_widget.setItem(2,2,QTableWidgetItem("100"))


app = QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())

