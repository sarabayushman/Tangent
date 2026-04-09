from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from screen import inactiveScreen, activeScreen

class WindowStacker(QStackedWidget):
    def __init__(self, MainApp):
        """ A QStackedWidget to hold different window screens, manage and switch between them """
        super().__init__()
        
        # Adding the different screens to the stacker
        self.addWidget(inactiveScreen.InactiveScreenWidget(MainApp))
        self.addWidget(activeScreen.ActiveScreenWidget(MainApp))

        self.setCurrentIndex(0) # Start with the inactive screen by default

    def setCurrentIndex(self, index):
        """ Override the setCurrentIndex method to perform any necessary setup whenever the current screen is changed. This allows each screen to perform any necessary setup whenever it becomes the current screen. """
        super().setCurrentIndex(index)
        self.widget(index).__initBeforeLoad__() # Call the __initBeforeLoad__ method of the new screen to perform any necessary setup always whenever WindowStacker's currentIndex is changed. This allows each screen to perform any necessary setup whenever it becomes the current screen.

        
class AppWindow(QMainWindow):
    def __init__(self):
        """ The main application window that will hold the WindowStacker and manage the overall application although itself is transparent and frameless """
        super().__init__()

        # Making the main window frameless and transparent
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("QMainWindow{background-color: transparent}")

        # Setting up the window stacker and adding it as a central widget
        self.windowStacker = WindowStacker(self)
        self.setCentralWidget(self.windowStacker)

app = QApplication([])
app_window = AppWindow()
app_window.show()
app.exec()