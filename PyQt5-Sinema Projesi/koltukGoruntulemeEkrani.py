from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QMenuBar, QAction, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import QSize, Qt

from biletSatisEkrani import BiletSatisEkrani
from data import filmListesi

class KoltukGoruntulemeEkrani(QWidget):
    def __init__(self,film):
        super().__init__()
        self.film=film
        self.secilenKoltuklar=[]


        self.setGeometry(300,200,1600,800)
        self.setWindowTitle(film.isim)
        self.pencereGoruntusunuOlustur()
        self.menuOlustur()

    def pencereGoruntusunuOlustur(self):
        layout=QVBoxLayout()
        self.grid=QGridLayout()

        for koltuk in self.film.koltukBilgileri:
            koltukNo=koltuk.koltukNo
            koltukDurumu=koltuk.koltukDurumu

            buton=QPushButton(f"{koltukNo}")
            buton.setFixedSize(QSize(160,80))
            buton.clicked.connect(self.biletSecCagrisi(koltukNo))

            if koltukDurumu:#1 ise alinmis.
                buton.setEnabled(False)
                buton.setStyleSheet("background-color: red; color:white;")
            else:
                buton.setEnabled(True)
                buton.setStyleSheet("background-color: green; color:white;")

            row, col = divmod(koltukNo-1,5)
            self.grid.addWidget(buton,row,col)

        self.biletAlButon = QPushButton("Bilet Al")
        self.biletAlButon.clicked.connect(self.biletAl)
        self.biletAlButon.setFixedSize(150,50)
        self.biletAlButon.setStyleSheet("background-color:gray;color:white")
        self.biletAlButon.setEnabled(False)

        layout.addLayout(self.grid)
        layout.addWidget(self.biletAlButon, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def biletSecCagrisi(self,secilenKoltukNo):
        def biletSec():
            secilenKoltuk=self.grid.itemAt(secilenKoltukNo-1).widget()#butonu elde ettim.

            #Koltugun secilmesi
            if secilenKoltukNo not in self.secilenKoltuklar:
                self.secilenKoltuklar.append(secilenKoltukNo)
                secilenKoltuk.setStyleSheet("background-color: yellow;color:white")
                if len(self.secilenKoltuklar)==1:
                    self.biletAlButon.setStyleSheet("background-color:green;color:white")
                    self.biletAlButon.setEnabled(True)
            #Secimin kaldirilmasi
            else:
                self.secilenKoltuklar.remove(secilenKoltukNo)
                secilenKoltuk.setStyleSheet("background-color: green; color:white")
                if len(self.secilenKoltuklar)==0:
                    self.biletAlButon.setStyleSheet("background-color:gray;color:white")
                    self.biletAlButon.setEnabled(False)
        return biletSec

    def biletAl(self):
        self.close()
        self.biletSatisEkran=BiletSatisEkrani(film=self.film,secilenKoltuklar=self.secilenKoltuklar)
        self.biletSatisEkran.show()

    def menuOlustur(self):
        menu_bar=QMenuBar(self)
        detayMenu=menu_bar.addMenu("Detay")

        biletGoruntuleAction=QAction("Biletleri Goruntule",self)
        biletGoruntuleAction.setShortcut("Ctrl+N")
        biletGoruntuleAction.triggered.connect(self.alinanBiletleriGoruntule)

        detayMenu.addAction(biletGoruntuleAction)

    def alinanBiletleriGoruntule(self):
        self.window=QWidget()
        self.window.setWindowTitle("Alinan Biletler")
        self.window.setGeometry(150,100,800,800)
        doluKoltuklar=self.doluKoltuklariBul()

        biletGoruntuleTable = QTableWidget(self.window)
        biletGoruntuleTable.setFixedSize(800,800)
        biletGoruntuleTable.setRowCount(len(doluKoltuklar)+1)
        biletGoruntuleTable.setColumnCount(3)

        #Header-Baslik
        koltukNoHeader = QTableWidgetItem("Koltuk No")
        koltukNoHeader.setBackground(QColor(255,0,0))
        biletGoruntuleTable.setItem(0,0,koltukNoHeader)

        alanKisiHeader = QTableWidgetItem("Alan Kisi")
        alanKisiHeader.setBackground(QColor(255,0,0))
        biletGoruntuleTable.setItem(0,1,alanKisiHeader)

        biletTutarHeader = QTableWidgetItem("Bilet Tutar")
        biletTutarHeader.setBackground(QColor(255,0,0))
        biletGoruntuleTable.setItem(0,2,biletTutarHeader)

        for index,koltuk in enumerate(doluKoltuklar):
            biletGoruntuleTable.setItem(index+1,0,QTableWidgetItem(str(koltuk.koltukNo)))
            biletGoruntuleTable.setItem(index+1,1,QTableWidgetItem(str(koltuk.alanKisi)))
            biletGoruntuleTable.setItem(index+1,2,QTableWidgetItem(str(koltuk.tutar)))
            
        self.window.show()
    def doluKoltuklariBul(self):
        doluKoltuklar=[]
        id=self.film.id
        for koltuk in filmListesi[id-1].koltukBilgileri:
            if koltuk.koltukDurumu==1:
                doluKoltuklar.append(koltuk)
        return doluKoltuklar
