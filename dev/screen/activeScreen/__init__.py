from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class ActiveScreenWidget(QWidget):
    def __init__(self, MainApp):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: yellow")

    def __initBeforeLoad__(self):
        """ A method to perform any setup to the screen whenever WindowStacker's currentIndex is changed to this screen. This method is automatically called with `WindowStacker.setCurrentIndex(int)` """
        pass
