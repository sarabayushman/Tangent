from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPoint, QPropertyAnimation, Qt

class ActiveScreenWidget(QWidget):
    def __init__(self, MainApp:QMainWindow):
        super().__init__()
        self.MainApp = MainApp # A reference to the main application window, which is passed in when the widget is created. This allows the widget to interact with the main application window, such as resizing or moving it.

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: rgba(255,255,255,150); border-radius: 10px;") 

    def __initBeforeLoad__(self):
        """ A method to perform any setup to the screen whenever WindowStacker's currentIndex is changed to this screen. This method is automatically called with `WindowStacker.setCurrentIndex(int)` """
        
        self.MainApp.resize(400, 300) 
        self.MainApp.move(self.MainApp.x(), -(self.MainApp.height()))
        self._animate_Onload()

    def _animate_Onload(self):
        """ A method to perform the animation of the screen sliding down from the top of the screen whenever it becomes the current screen. This method is called in the __initBeforeLoad__ method to perform the animation whenever the screen becomes the current screen. """

        # Animate the main application window sliding down from the top of the screen
        self.animation = QPropertyAnimation(self.MainApp, b"pos")
        self.animation.setDuration(100) # Duration of the animation in milliseconds
        self.animation.setStartValue(self.MainApp.pos()) 
        self.animation.setEndValue(QPoint(self.MainApp.x(), 3)) 
        self.animation.start()
    
    def _animate_Onclose(self):
        """ A method to perform the animation of the screen sliding up to the top of the screen whenever it is closed. This method can be called whenever you want to close the screen with an animation. """

        # Animate the main application window sliding up to the top of the screen
        self.animation = QPropertyAnimation(self.MainApp, b"pos")
        self.animation.setDuration(100) # Duration of the animation in milliseconds
        self.animation.setStartValue(self.MainApp.pos()) 
        self.animation.setEndValue(QPoint(self.MainApp.x(), -(self.MainApp.height()))) 
        self.animation.start()

    def mousePressEvent(self, event):
        """Handle mouse press events to close the screen if clicked outside the widget."""
        if not self.rect().contains(self.mapFromGlobal(event.globalPos())):
            self._animate_Onclose()
    


if __name__ == "__main__":
    import os
    os.system("python ./dev/main.py")
