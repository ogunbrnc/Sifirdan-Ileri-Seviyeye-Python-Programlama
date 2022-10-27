import sys
from PyQt5.QtWidgets import QApplication

from girisEkrani import GirisEkrani

#uygulama olusturduk
app=QApplication(sys.argv)
girisEkrani=GirisEkrani()
girisEkrani.show()

#uygulamayı donguye aldik
sys.exit(app.exec_())