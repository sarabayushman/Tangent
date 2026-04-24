import sys
from PyQt5.QtWidgets import QApplication, QGraphicsDropShadowEffect, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from PyQt5.uic import loadUi

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('.\\dev\\scripts\\simpleWindow\\simpleWindow.ui', self)

        # Making the main window frameless and transparent
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.WIN_RESIZE_VH_WIDGET.setAttribute(Qt.WA_TranslucentBackground)

        # Adding a drop shadow effect to the visible window to give it a more polished and modern look, making it stand out against the transparent background and enhancing the overall visual appeal of the application.
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setColor(QColor(70, 70, 70, 160))
        shadow.setOffset(0, 0)
        self.visibleWin.setGraphicsEffect(shadow)

        # for window resize
        self.ENABLE_MOUSETRACK_WINRESIZE_TYPE = None
    
    def setCanvasUI(self, UI_file:str):
        loadUi(UI_file, self.canvas)

    ################ Window Resize ################

    def mousePressEvent(self, event):
        child = self.childAt(event.pos())
        if child == self.WIN_RESIZE_V_WIDGET:
            self.ENABLE_MOUSETRACK_WINRESIZE_TYPE = 'V'
        elif child == self.WIN_RESIZE_H_WIDGET:
            self.ENABLE_MOUSETRACK_WINRESIZE_TYPE = 'H'
        elif child == self.WIN_RESIZE_VH_WIDGET:
            self.ENABLE_MOUSETRACK_WINRESIZE_TYPE = 'VH'

    def mouseMoveEvent(self, event):
        if self.ENABLE_MOUSETRACK_WINRESIZE_TYPE == 'V':
            new_height = max(self.minimumHeight(), event.globalY() - self.frameGeometry().top())
            self.MainApp.resize(self.width(), new_height)
        elif self.ENABLE_MOUSETRACK_WINRESIZE_TYPE == 'H':
            new_width = max(self.minimumWidth(), event.globalX() - self.frameGeometry().left())
            self.MainApp.resize(new_width, self.height())
        elif self.ENABLE_MOUSETRACK_WINRESIZE_TYPE == 'VH':
            new_width = max(self.minimumWidth(), event.globalX() - self.frameGeometry().left())
            new_height = max(self.minimumHeight(), event.globalY() - self.frameGeometry().top())
            self.MainApp.resize(new_width, new_height)

    def mouseReleaseEvent(self, event):
        self._size = [self.width(), self.height()]
        self.ENABLE_MOUSETRACK_WINRESIZE_TYPE = None

    ###############################################
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleWindow()
    window.show()
    sys.exit(app.exec_())
        