from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class AgentWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("./dev/screen/activeScreen/menu/agentsMenu/agentWidget.ui", self)