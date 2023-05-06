# imports
from utils.widgets import *


class Button(QToolButton):
    
    def __init__(self, *args, **kargs) -> None:
        super(Button, self).__init__(*args, **kargs)

class TitleBar(QFrame):
    
    def __init__(self, *args, **kargs) -> None:
        super(TitleBar, self).__init__(*args, **kargs)
        
        # main parameters
        self.root = kargs['parent']
        self.pressed = False
        
        # widget settings
        self.setFixedHeight(20)
        self.setStyleSheet('background: #d6d6d6')
        
        # widget layout
        exitButton = Button()
        exitButton.clicked.connect(self.exitCall)
        
        maxButton = Button()
        maxButton.clicked.connect(self.maxCall)
        
        minButton = Button()
        minButton.clicked.connect(self.minCall)
        
        mainLayout = QHBoxLayout()
        mainLayout.setContentsMargins(0,0,0,0)
        mainLayout.setSpacing(0)
        mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignRight)
        mainLayout.addWidget(minButton)
        mainLayout.addWidget(maxButton)
        mainLayout.addWidget(exitButton)
        self.setLayout(mainLayout)
    
    def exitCall(self) -> None:
        self.root.close()
    
    def minCall(self) -> None:
        if self.root.isMinimized():
            self.root.showNormal()
        else:
            self.root.showMinimized()
    
    def maxCall(self) -> None:
        if self.root.isFullScreen():
            self.root.showNormal()
        else:
            self.root.showFullScreen()
    
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