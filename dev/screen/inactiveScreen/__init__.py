from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

class InactiveScreenWidget(QWidget):
    def __init__(self, MainApp: QMainWindow):
        super().__init__()
        self.MainApp = MainApp # A reference to the main application window, which is passed in when the widget is created. This allows the widget to interact with the main application window, such as resizing or moving it.

        # Making the widget transparent and allowing it to have a styled background for the UI file 
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Load the UI file 
        loadUi("./dev/screen/inactiveScreen/inactiveScreen.ui", self)

    def __initBeforeLoad__(self):
        """ A method to perform any setup to the screen whenever WindowStacker's currentIndex is changed to this screen. This method is automatically called with `WindowStacker.setCurrentIndex(int)` """
        self.MainApp.resize(70, 8)
        self.MainApp.move(5, 0)

    def mousePressEvent(self, event):
        """ Override the mousePressEvent to allow changing to the active screen when the inactive screen is clicked """

        super().mousePressEvent(event)

        if event.button() == Qt.LeftButton:
            self.MainApp.windowStacker.setCurrentIndex(1) # Switch to the active screen (index 1 in the stack)
            event.accept()



if __name__ == "__main__":
    app = QApplication([])
    window = InactiveScreenWidget(None)
    window.show()
    app.exec()