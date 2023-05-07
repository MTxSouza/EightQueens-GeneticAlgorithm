# imports
from utils.widgets import *


class OptionFrame(QFrame):
    
    def __init__(self, *args, **kargs) -> None:
        super().__init__(*args, **kargs)
        
        # widget settings
        self.setFixedWidth(250)
    
    def paintEvent(self, arg__1: QPaintEvent) -> None:
        
        with QPainter(self) as painter:
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            
            painter.setBrush(QColor('#c2c2c2'))
            
            rect = self.rect()
            painter.drawRoundedRect(rect, 30, 30)

class MainFrame(QFrame):
    
    def __init__(self, *args, **kargs) -> None:
        super(MainFrame, self).__init__(*args, **kargs)
        
        # widget settings
        self.setStyleSheet('background: #d6d6d6')
        
        # widget layout
        optionsFrame = OptionFrame()
        
        gameFrame = QFrame()
        gameFrame.setStyleSheet('background: red')
        
        mainLayout = QHBoxLayout()
        mainLayout.setContentsMargins(30,50,30,50)
        mainLayout.setSpacing(30)
        mainLayout.addWidget(optionsFrame)
        mainLayout.addWidget(gameFrame)
        self.setLayout(mainLayout)