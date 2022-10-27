import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMenuBar, QAction
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("QMenu")
        self.setWindowIcon(QIcon('python.png'))

        menu_bar = QMenuBar(self)

        fileMenu = menu_bar.addMenu("File")
        editMenu = menu_bar.addMenu("Edit")
        selectionMenu = menu_bar.addMenu("Selection")

        newTextFileAction = QAction(QIcon('python.png'),"New Text File",self)
        newTextFileAction.setShortcut("Ctrl+N")
        newTextFileAction.triggered.connect(self.newTextFileActionTiklandi)

        undoAction = QAction(QIcon('python.png'),"Undo",self)
        undoAction.setShortcut("Ctrl+Z")
        undoAction.triggered.connect(self.undoTetiklendi)

        fileMenu.addAction(newTextFileAction)
        editMenu.addAction(undoAction)
        fileMenu.addMenu(editMenu)

    def newTextFileActionTiklandi(self):
        print("New Text File Action Tiklandi")

    def undoTetiklendi(self):
        print("Unfo Tiklandi")


app = QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())

