from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("./dev/screen/activeScreen/menu/searchMenu/searchWidget.ui", self)