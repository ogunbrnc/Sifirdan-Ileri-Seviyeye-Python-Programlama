import json

class Koltuk:
    def __init__(self,koltukNo,koltukDurumu,alanKisi,tutar):
        self.koltukNo=koltukNo
        self.koltukDurumu=koltukDurumu
        self.alanKisi=alanKisi
        self.tutar=tutar

class Film:
    def __init__(self,isim,resimYolu,id,koltukBilgileri):
        self.isim=isim
        self.resimYolu=resimYolu
        self.id=id
        self.koltukBilgileri=koltukBilgileri



def veriyiAl():
    dosya=open("data.json")
    veri=json.load(dosya)
    filmListesi=[]# 6 film burada tum bilgileriyle saklanacak.
    for filmIsmi in veri.keys():
        film=veri[filmIsmi]
        koltukBilgileri=[Koltuk(koltuk['koltukNo'],koltuk['koltukDurumu'],koltuk['alanKisi'],koltuk['tutar']) for koltuk in film['koltukBilgileri']]
        filmListesi.append(Film(filmIsmi, film['image'], film['id'],koltukBilgileri))
    return filmListesi

filmListesi=veriyiAl()
    

        