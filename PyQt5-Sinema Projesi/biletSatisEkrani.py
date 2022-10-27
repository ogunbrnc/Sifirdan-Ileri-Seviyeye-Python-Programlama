from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QRadioButton, QMessageBox

from data import filmListesi
import json

class BiletSatisEkrani(QWidget):
    def __init__(self,film,secilenKoltuklar):
        super().__init__()
        self.film=film
        self.secilenKoltuklar=secilenKoltuklar
        self.lineEditListesi=[]

        self.secilenKoltukSayisi=len(secilenKoltuklar)
        self.toplamTutar=20.0*self.secilenKoltukSayisi
        dinamikFormUzunlugu=self.secilenKoltukSayisi*180

        self.setFixedSize(400,dinamikFormUzunlugu)
        self.setWindowTitle(film.isim)

        self.formOlustur()

    def formOlustur(self):
        layout=QVBoxLayout()

        for koltukNo in self.secilenKoltuklar:
            koltukNoLabel=QLabel()
            koltukNoLabel.setText(f"Koltuk No:{koltukNo}")
            layout.addWidget(koltukNoLabel)

            hBoxKullaniciBilgisi=QHBoxLayout()
            isimSoyisimLabel=QLabel("Isim Soyisim:")
            isimSoyisimLineEdit=QLineEdit()
            self.lineEditListesi.append(isimSoyisimLineEdit)

            hBoxKullaniciBilgisi.addWidget(isimSoyisimLabel)
            hBoxKullaniciBilgisi.addWidget(isimSoyisimLineEdit)

            layout.addLayout(hBoxKullaniciBilgisi)
        
        hboxBiletBilgisi=QHBoxLayout()

        tamBiletRadioButton=QRadioButton("Tam Bilet")
        tamBiletRadioButton.setChecked(True)
        tamBiletRadioButton.toggled.connect(self.biletTuruSecildi)

        ogrenciBiletRadioButton=QRadioButton("Ogrenci Bileti")
        ogrenciBiletRadioButton.toggled.connect(self.biletTuruSecildi)

        hboxBiletBilgisi.addWidget(tamBiletRadioButton)
        hboxBiletBilgisi.addWidget(ogrenciBiletRadioButton)
        layout.addLayout(hboxBiletBilgisi)


        self.toplamTutarLabel=QLabel()
        self.toplamTutarLabel.setText(f"Toplam Tutar: {self.toplamTutar} ")
        layout.addWidget(self.toplamTutarLabel)

        self.biletAlButon=QPushButton("Bilet Al")
        self.biletAlButon.clicked.connect(self.biletAlTiklandi)
        layout.addWidget(self.biletAlButon)

        self.setLayout(layout)

    def biletTuruSecildi(self):
        radio_button=self.sender()
        if radio_button.isChecked() and radio_button.text()=="Ogrenci Bileti":
            self.toplamTutar-=5.0*self.secilenKoltukSayisi
        elif radio_button.isChecked() and radio_button.text()=="Tam Bilet":
            self.toplamTutar+=5.0*self.secilenKoltukSayisi
        self.toplamTutarLabel.setText(f"Toplam Tutar: {self.toplamTutar}")
        

    def biletAlTiklandi(self):
        for lineEdit in self.lineEditListesi:
            if len(lineEdit.text())==0:
                QMessageBox.warning(self,"HATA!","Eksik bilgiler mevcut.")
                return
        kullaniciCevabi=QMessageBox.question(self,"Bilet Satis",f"Toplam tutar: {self.toplamTutar}. Bilet alimini onayliyor musunuz?",QMessageBox.Yes | QMessageBox.No)
        if kullaniciCevabi == QMessageBox.Yes:
            self.biletAl()
    
    def biletAl(self):
        dosya=open("data.json","r")#dosyayi okumak icin actik
        veri=json.load(dosya)#veriyi aldik
        dosya.close()#dosyayi kapattik.

        for index, lineEdit in enumerate(self.lineEditListesi):
            secilenKoltukNo=self.secilenKoltuklar[index]

            veri[f"{self.film.isim}"]["koltukBilgileri"][secilenKoltukNo-1]["koltukDurumu"]=1
            veri[f"{self.film.isim}"]["koltukBilgileri"][secilenKoltukNo-1]["alanKisi"]=lineEdit.text()
            veri[f"{self.film.isim}"]["koltukBilgileri"][secilenKoltukNo-1]["tutar"]=self.toplamTutar/self.secilenKoltukSayisi

            id=self.film.id
            filmListesi[id-1].koltukBilgileri[secilenKoltukNo-1].koltukDurumu=1
            filmListesi[id-1].koltukBilgileri[secilenKoltukNo-1].alanKisi=lineEdit.text()
            filmListesi[id-1].koltukBilgileri[secilenKoltukNo-1].tutar=self.toplamTutar/self.secilenKoltukSayisi

        dosya=open("data.json","w")
        dosya.write(json.dumps(veri,indent=4))
        dosya.close()
        
        QMessageBox.information(self,"Basarili", "Bilet basariyla alindi!")
        self.close()

        