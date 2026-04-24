from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPoint, QEvent, QEasingCurve, QPropertyAnimation, QTimer, Qt
from PyQt5.QtGui import QColor
from PyQt5.uic import loadUi
from screen.activeScreen.menu import chatMenu, agentsMenu, searchMenu, dockMenu, settingsMenu
from scripts.simpleWindow import SimpleWindow

class ActiveScreenWidget(SimpleWindow):
    def __init__(self, MainApp:QMainWindow):
        super().__init__()
        self.MainApp = MainApp # A reference to the main application window, which is passed in when the widget is created. This allows the widget to interact with the main application window, such as resizing or moving it.

        self.animation = None # A reference to the current animation, which is used to perform the sliding animation when the screen is shown or hidden. This allows the widget to keep track of the current animation and ensure that it is properly managed and stopped when necessary.
        self._is_closing = False # A flag to indicate whether the screen is currently in the process of closing. This is used to prevent multiple close animations from being triggered simultaneously, which could cause unexpected behavior or visual glitches.
        self._ready_to_close = False # A flag to indicate whether the screen is ready to be closed. This is used to ensure that the close animation is only triggered when the screen is fully loaded and ready, preventing premature closing or visual glitches.

        self._size = [670, 420] # The size of the active screen, which is used to set the size of the main application window when the active screen is shown. This allows the active screen to have a specific size that is different from the inactive screen, providing a more tailored user experience.

        # ---------------------- setting ui ----------------------

        self.setCanvasUI('./dev/screen/activeScreen/activeScreenDesign.ui') # loading the UI file

        #---------------------- other ----------------------

        self.setAttribute(Qt.WA_StyledBackground, True) # Making the widget transparent and allowing it to have a styled background for the UI file
        self.MainApp.installEventFilter(self) # Install an event filter on the main application window to detect when it loses focus, which will trigger the close animation for the active screen. This allows the active screen to automatically close when the user clicks outside of it or switches to another application, providing a seamless user experience.

        # ---------------------- setting the button onclick event ----------------------

        self.activeMenu = None
        self.MenuBtnContainer = self.visibleWin.children()[1].widgeto
        for i, child in enumerate(self.MenuBtnContainer.children()): # Debug print statement to show the child widgets of the visibleWin widget. This can be helpful for debugging and ensuring that the child widgets are being loaded correctly from the UI file.
            if i != 0:
                # print(f"{child.objectName()}: {child}")
                child.clicked.connect(lambda _, btn=child: self.changed_menu(btn))
            if i == 1:
                self.activeMenu = child # Setting the activeMenu variable to the first button in the visibleWin widget, which is the menu button that will be used to switch between different menus in the active screen. This allows the active screen to have a specific menu button that can be easily accessed and interacted with by the user.

        # --------------------- setting ActiveMenuWidget ----------------------

        self.menuStackedWidget = QStackedWidget() #defining
        self.menuStackedWidget.setStyleSheet(open("./dev/screen/activeScreen/style.qss", 'r').read()) # the style

        self.menuStackedWidget.addWidget(chatMenu.ChatWidget())
        self.menuStackedWidget.addWidget(agentsMenu.AgentWidget())
        self.menuStackedWidget.addWidget(searchMenu.SearchWidget())
        self.menuStackedWidget.addWidget(dockMenu.DockWidget())
        self.menuStackedWidget.addWidget(settingsMenu.SettingsWidget())

        self.menuStackedWidget.setCurrentIndex(0)

        self.visibleWin.children()[1].children()[0].addWidget(self.menuStackedWidget)

        # ----------------------------------------------------------------------


    def __initBeforeLoad__(self):
        """ A method to perform any setup to the screen whenever WindowStacker's currentIndex is changed to this screen. This method is automatically called with `WindowStacker.setCurrentIndex(int)` """
        #-------------
        # self.MainApp.resize(400, 300) 
        self.MainApp.resize(*self._size) 
        self.MainApp.move(self.MainApp.x(), -(self.MainApp.height()))
        #-------------
        self._is_closing = False
        self._ready_to_close = False
        self._animate_Onload()
        self.MainApp.show()
        self.MainApp.raise_()
        self.MainApp.activateWindow()
        QTimer.singleShot(0, self._enable_close_detection)
    
    ############################### Menu changes ###############################
    
    def changed_menu(self, menuBtn):
        self.activeMenu.setStyleSheet("QPushButton{background-color: transparent;color: rgba(0,0,0,0.6);border-radius: 10px;}QPushButton:hover{border:1px solid grey;}")
        self.activeMenu = menuBtn
        self.activeMenu.setStyleSheet("background-color: white;color: black;border: none;border-radius: 10px;")
        self.menuStackedWidget.setCurrentIndex(int(menuBtn.objectName()[1]))
        print(int(menuBtn.objectName()[1]))

    ############################### Animations ###############################

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

    ############################### ---  ###############################

