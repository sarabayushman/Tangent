from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

class InactiveScreenWidget(QWidget):
    def __init__(self, MainApp: QMainWindow):
        super().__init__()
        self.MainApp = MainApp # A reference to the main application window, which is passed in when the widget is created. This allows the widget to interact with the main application window, such as resizing or moving it.

        # Making the widget transparent and allowing it to have a styled background for the UI file 
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.setAcceptDrops(True) # Essential to enable drops

        # Load the UI file 
        loadUi("./dev/screen/inactiveScreen/inactiveScreen.ui", self)

    ######################### Setup whenever current screen #########################

    def __initBeforeLoad__(self):
        """ A method to perform any setup to the screen whenever WindowStacker's currentIndex is changed to this screen. This method is automatically called with `WindowStacker.setCurrentIndex(int)` """
        self.MainApp.resize(70, 8)
        self.MainApp.move(5, 0)

    ######################### Change to active screen on click #########################

    def mousePressEvent(self, event):
        """ Override the mousePressEvent to allow changing to the active screen when the inactive screen is clicked """

        super().mousePressEvent(event)

        if event.button() == Qt.LeftButton:
            self.MainApp.windowStacker.setCurrentIndex(1) # Switch to the active screen (index 1 in the stack)
            event.accept()

    ######################### Drag and Drop file/text to Dock #########################
    def dragEnterEvent(self, event):
        """Check if the drag contains file URLs or text to add it into the File/text Docker"""
        if event.mimeData().hasUrls() or event.mimeData().hasText():
            event.accept()

            self.widget.setMinimumHeight(110) # Increase the minimum height to allow space for the drop indication when dragging files over the widget

            # color bug fix
            self.widget.setStyleSheet("QWidget{background-color: rgba(238, 51, 255, 255);border-bottom-left-radius: 8px;border-bottom-right-radius: 8px;}QWidget:hover{background-color: rgba(238, 51, 255, 255);}")

        else:
            event.ignore()

    def dropEvent(self, event):
        """Extract local file paths and text-content from dropped URLs and text"""
        self.widget.setMinimumHeight(10) # Reset the minimum height to its original value 

        mime = event.mimeData()
        
        # 1. Handle Files
        if mime.hasUrls():
            for url in mime.urls():
                print(f"Dropped File: {url.toLocalFile()}")
        
        # 2. Handle Text (from a browser, notepad, etc.)
        elif mime.hasText():
            print(f"Dropped Text: {mime.text()}")

        # color bug fix
        self.widget.setStyleSheet("QWidget{background-color: rgba(238, 51, 255, 98);border-bottom-left-radius: 8px;border-bottom-right-radius: 8px;}QWidget:hover{background-color: rgba(238, 51, 255, 255);}")
        
    ######################### ######################### #########################
    

if __name__ == "__main__":
    app = QApplication([])
    window = InactiveScreenWidget(None)
    window.show()
    app.exec()