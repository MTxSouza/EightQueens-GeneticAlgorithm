# imports
from utils.widgets import *


class Button(QToolButton):
    
    def __init__(self, icon: str, *args, **kargs) -> None:
        super(Button, self).__init__(*args, **kargs)
        
        # main parameters
        self.ic = icon
        
        # widget settings
        self.setFixedWidth(40)
    
    def paintEvent(self, arg__1: QPaintEvent) -> None:
        
        # creating painter
        with QPainter(self) as painter:
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            
            if self.underMouse():
                if self.ic == 'exit':
                    painter.setBrush(QColor('#f13232'))
                    iconColor = QColor('#ffffff')
                else:
                    painter.setBrush(QColor('#c2c2c2'))
                    iconColor = QColor('#474747')
            else:
                painter.setBrush(QColor('#d6d6d6'))
                iconColor = QColor('#474747')
            
            rect = self.rect()
            painter.drawRect(rect)
            
            cx = int((self.rect().x() + self.rect().width()) / 2)
            cy = int((self.rect().y() + self.rect().height()) / 2)
            
            pen = QPen()
            pen.setWidthF(1.5)
            pen.setColor(iconColor)
            
            painter.setPen(pen)
            if self.ic == 'exit':
                painter.drawLines([
                    QLine(cx-4, cy-4, cx+4, cy+4),
                    QLine(cx-4, cy+4, cx+4, cy-4),
                ])
            elif self.ic == 'min':
                painter.drawLine(QLine(cx-5, cy, cx+5, cy))
            elif self.ic == 'max':
                painter.drawLines([
                    QLine(cx-5, cy-2, cx+5, cy-2),
                    QLine(cx+5, cy-2, cx+5, cy+2),
                    QLine(cx+5, cy+2, cx-5, cy+2),
                    QLine(cx-5, cy+2, cx-5, cy-2),
                ])

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
        exitButton = Button(icon='exit')
        exitButton.clicked.connect(self.exitCall)
        
        maxButton = Button(icon='max')
        maxButton.clicked.connect(self.maxCall)
        
        minButton = Button(icon='min')
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