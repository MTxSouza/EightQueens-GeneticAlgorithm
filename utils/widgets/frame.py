# imports
from utils.widgets import *


class MainFrame(QFrame):
    
    def __init__(self, *args, **kargs) -> None:
        super(MainFrame, self).__init__(*args, **kargs)
        
        # widget settings
        self.setStyleSheet('background: #d6d6d6')
        
        # widget layout
        optionsFrame = QFrame()
        optionsFrame.setStyleSheet('background: blue')
        optionsFrame.setFixedWidth(250)
        
        gameFrame = QFrame()
        gameFrame.setStyleSheet('background: red')
        
        mainLayout = QHBoxLayout()
        mainLayout.setContentsMargins(0,0,0,0)
        mainLayout.setSpacing(0)
        mainLayout.addWidget(optionsFrame)
        mainLayout.addWidget(gameFrame)
        self.setLayout(mainLayout)