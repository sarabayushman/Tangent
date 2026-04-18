"""
This is the main entry point of the application. It sets up the main application window, which is transparent and frameless, and contains a WindowStacker that manages different screens (inactive and active). The WindowStacker allows switching between these screens and ensures that any necessary setup is performed whenever a screen becomes active. The main application window is designed to stay on top of other windows, providing a seamless user experience.

## Notations
-> `MainApp`: Refers to the main application window (an instance of AppWindow) that is passed to the screen widgets. This allows the screen widgets to interact with the main application window, such as resizing or moving it.

-> `screen`: Refers to the different screens (inactive and active) that are managed by the WindowStacker. Each screen is a QWidget that can perform its own setup whenever it becomes the current screen in the stacker.
    -> `inactiveScreen`: The screen that is shown when the application is not active. It allows the user to click on it to switch to the active screen and also supports drag-and-drop functionality for files and text.
    -> `activeScreen`: The screen that is shown when the application is active. It performs a sliding animation when it becomes active and can be closed by clicking outside of it, which triggers a sliding animation to close it.

-> `WindowStacker`: A QStackedWidget that holds the different screens and manages switching between them. It overrides the setCurrentIndex method to perform any necessary setup whenever the current screen is changed.

Note: The code is structured to allow for easy addition of new screens in the future by simply adding new QWidget classes and adding them to the WindowStacker. Each screen can have its own unique setup and behavior while still being managed by the main application window.
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
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