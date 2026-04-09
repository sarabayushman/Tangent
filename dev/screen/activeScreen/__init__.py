from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPoint, QEvent, QEasingCurve, QPropertyAnimation, QTimer, Qt

class ActiveScreenWidget(QWidget):
    def __init__(self, MainApp:QMainWindow):
        super().__init__()
        self.MainApp = MainApp # A reference to the main application window, which is passed in when the widget is created. This allows the widget to interact with the main application window, such as resizing or moving it.
        self.animation = None # A reference to the current animation, which is used to perform the sliding animation when the screen is shown or hidden. This allows the widget to keep track of the current animation and ensure that it is properly managed and stopped when necessary.
        self._is_closing = False # A flag to indicate whether the screen is currently in the process of closing. This is used to prevent multiple close animations from being triggered simultaneously, which could cause unexpected behavior or visual glitches.
        self._ready_to_close = False # A flag to indicate whether the screen is ready to be closed. This is used to ensure that the close animation is only triggered when the screen is fully loaded and ready, preventing premature closing or visual glitches.

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: rgba(255,255,255,150); border-radius: 10px;") 

        self.MainApp.installEventFilter(self)

    def __initBeforeLoad__(self):
        """ A method to perform any setup to the screen whenever WindowStacker's currentIndex is changed to this screen. This method is automatically called with `WindowStacker.setCurrentIndex(int)` """
        #-------------
        self.MainApp.resize(400, 300) 
        self.MainApp.move(self.MainApp.x(), -(self.MainApp.height()))
        #-------------
        self._is_closing = False
        self._ready_to_close = False
        self._animate_Onload()
        self.MainApp.show()
        self.MainApp.raise_()
        self.MainApp.activateWindow()
        QTimer.singleShot(0, self._enable_close_detection)

    def eventFilter(self, obj, event):
        """Close the active screen when the window loses focus."""
        if obj is not self.MainApp:
            return super().eventFilter(obj, event)

        if self.MainApp.windowStacker.currentIndex() != 1 or self._is_closing or not self._ready_to_close:
            return super().eventFilter(obj, event)

        if event.type() == QEvent.WindowDeactivate:
            self._animate_Onclose()

        return super().eventFilter(obj, event)

    def _enable_close_detection(self):
        self._ready_to_close = True

    def _animate_Onload(self):
        """ A method to perform the animation of the screen sliding down from the top of the screen whenever it becomes the current screen. This method is called in the __initBeforeLoad__ method to perform the animation whenever the screen becomes the current screen. """
        self.animation = QPropertyAnimation(self.MainApp, b"pos")
        self.animation.setDuration(140) # Duration of the animation in milliseconds
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.setStartValue(self.MainApp.pos()) 
        self.animation.setEndValue(QPoint(self.MainApp.x(), 3)) 
        self.animation.start()
    
    def _animate_Onclose(self):
        """ A method to perform the animation of the screen sliding up to the top of the screen whenever it is closed. This method can be called whenever you want to close the screen with an animation. """
        if self._is_closing:
            return

        self._is_closing = True
        self._ready_to_close = False
        self.animation = QPropertyAnimation(self.MainApp, b"pos")
        self.animation.setDuration(140) # Duration of the animation in milliseconds
        self.animation.setEasingCurve(QEasingCurve.InCubic)
        self.animation.setStartValue(self.MainApp.pos()) 
        self.animation.setEndValue(QPoint(self.MainApp.x(), -(self.MainApp.height()))) 
        self.animation.finished.connect(self._finish_close)
        self.animation.start()

    def _finish_close(self):
        self._is_closing = False
        if self.MainApp.windowStacker.currentIndex() == 1:
            self.MainApp.windowStacker.setCurrentIndex(0)

    
if __name__ == "__main__":
    import os
    os.system("python ./dev/main.py")
