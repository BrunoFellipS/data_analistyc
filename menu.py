from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import getpass
from time import sleep as soninho

class MenuPrincipal:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.window = uic.loadUi(r'D:\visualcode\data_analistyc\uis\first\form.ui')
        self.user = getpass.getuser()
        

if __name__ == '__main__':
    MP = MenuPrincipal()
    MP.window.show()
    MP.app.exec_()
