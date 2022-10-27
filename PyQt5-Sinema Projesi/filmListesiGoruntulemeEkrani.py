from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

from koltukGoruntulemeEkrani import KoltukGoruntulemeEkrani
from data import filmListesi

class FilmListesiGoruntulemeEkrani(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sinema Bilet")
        self.setFixedSize(1600,800)
        self.filmListesiUIOlustur()

    def filmListesiUIOlustur(self):
        grid = QGridLayout()
        for index, film in enumerate(filmListesi):
            resimYolu=film.resimYolu
            buton = QPushButton()
            buton.setIcon(QIcon(f"FilmAfisleri/{resimYolu}"))
            buton.setIconSize(QSize(300,300))
            buton.setFixedSize(QSize(300,300))
            buton.setStyleSheet("background-color:black;")
            buton.clicked.connect(self.filmTiklandiCagrisi(film))

            # 1.film -> 0.indeks [0 0]  row=0 col=0
            # 2.film -> 1.indeks [0 1]  row=0 col=1
            # 3.film -> 2.indeks [0 2]  row=0 col=2
            # 4.film -> 3.indeks [1 0]  row=1 col=0
            # 5.film -> 4.indeks [1 1]  row=1 col=1
            # 6.film -> 5.indeks [1 2]  row=1 col=2

            #3 deme sebebimiz her satir da 3 film istedigimiz icin.
            row, col = divmod(index,3)
            grid.addWidget(buton,row,col)
        self.setLayout(grid)

    def filmTiklandiCagrisi(self,film):
        def filmTiklandi():
            self.koltukGoruntulemeEkrani= KoltukGoruntulemeEkrani(film=film)
            self.koltukGoruntulemeEkrani.show()
        return filmTiklandi





           


    


    