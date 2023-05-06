# imports
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *



class TitleBar(QFrame):
    
    def __init__(self, *args, **kargs) -> None:
        super(TitleBar, self).__init__(*args, **kargs)
        
        # main parameters
        self.root = kargs['parent']
        self.pressed = False
        
        # widget settings
        self.setFixedHeight(30)
        self.setStyleSheet('background: blue')
    
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.pressed = True
            self.mousePressedPos = event.globalPos()
            self.windPos = self.root.pos()
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.pressed and not self.root.isFullScreen():
            globalPos = event.globalPos()
            movement = globalPos - self.mousePressedPos
            newPos = self.windPos + movement
            self.root.move(newPos)
            self.update()
    
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.pressed = False