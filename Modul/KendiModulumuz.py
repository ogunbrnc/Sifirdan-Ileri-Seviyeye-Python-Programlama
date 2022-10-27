class Ogrenci:
    def __init__(self,isim,soyisim,bolum):
        self.isim=isim
        self.soyisim=soyisim
        self.bolum=bolum
        print("Ogrenci Olusturuldu")
    def bilgileriYazdir(self):
        print("Isim:",self.isim)
        print("Soyisim:",self.soyisim)
        print("Bolum:",self.bolum)
        