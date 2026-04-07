from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class ActiveScreenWidget(QWidget):
    def __init__(self, MainApp):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: yellow")