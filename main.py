import sys
from PyQt5.QtWidgets import QApplication
from Dashboard import Gui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = Gui()
    mw.show()
    app.exec_()