from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox, QLabel
from PyQt5.QtCore import QSize, Qt

from filmListesiGoruntulemeEkrani import FilmListesiGoruntulemeEkrani

kullaniciAdi="ogunbrnc"
sifre="123456"

class GirisEkrani(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bilet Satis")
        self.setFixedSize(400,150)

        vbox = QVBoxLayout()

        hboxKullaniciAdi = QHBoxLayout()
        self.kullaniciAdiLabel=QLabel("Kullanici Adi: ")
        self.kullaniciAdiLineEdit=QLineEdit()
        self.kullaniciAdiLineEdit.setFixedSize(QSize(200,20))
        hboxKullaniciAdi.addWidget(self.kullaniciAdiLabel)
        hboxKullaniciAdi.addWidget(self.kullaniciAdiLineEdit)

        hboxSifre=QHBoxLayout()
        self.sifreLabel = QLabel("Sifre: ")
        self.sifreLineEdit=QLineEdit()
        self.sifreLineEdit.setFixedSize(QSize(200,20))
        self.sifreLineEdit.setEchoMode(QLineEdit.Password)
        hboxSifre.addWidget(self.sifreLabel)
        hboxSifre.addWidget(self.sifreLineEdit)

        self.buton= QPushButton()
        self.buton.setText("Giris Yap")
        self.buton.setFixedSize(100,30)
        self.buton.clicked.connect(self.girisYap)


        vbox.addLayout(hboxKullaniciAdi)
        vbox.addLayout(hboxSifre)
        vbox.addWidget(self.buton,alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(vbox)

    def girisYap(self):
        if self.kullaniciAdiLineEdit.text()==kullaniciAdi and self.sifreLineEdit.text()==sifre:
            self.close()#giris ekraninin kapanmasi icin
            self.filmListesiGoruntulemeEkrani=FilmListesiGoruntulemeEkrani()
            self.filmListesiGoruntulemeEkrani.show()
        else:
            QMessageBox.warning(self,"HATA", "Kullanici bilgileri hatali.")
