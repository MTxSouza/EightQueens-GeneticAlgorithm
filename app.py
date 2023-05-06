# imports
from utils.widgets import *


class EightQueensGame(QMainWindow):
    
    def __init__(self, *args, **kargs) -> None:
        super(EightQueensGame, self).__init__(*args, **kargs)
        
        # widget settings
        self.setMinimumSize(QSize(1280,720))
        self.setStyleSheet('background: #d6d6d6')
        
        # window layout
        titleBar = QFrame()
        titleBar.setFixedHeight(30)
        titleBar.setStyleSheet('background: blue')
        
        mainFrame = QFrame()
        mainFrame.setStyleSheet('background: red')
        
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(2,2,2,2)
        mainLayout.setSpacing(0)
        mainLayout.addWidget(titleBar)
        mainLayout.addWidget(mainFrame)
        
        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)
        
        self.setCentralWidget(mainWidget)
        
        self.show()


if __name__=='__main__':
    
    app = QApplication()
    gui = EightQueensGame()
    exit(code=app.exec())