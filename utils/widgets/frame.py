# imports
from utils.widgets import *


class Slider(QSlider):
    
    def __init__(self, min: int, max: int, isFloat: bool, *args, **kargs):
        super(Slider, self).__init__(*args, **kargs)
        
        # widget settings
        self.setOrientation(Qt.Orientation.Horizontal)
        self.setRange(min, max)
        
        # main parameters
        self.f = isFloat
    
    def paintEvent(self, event):
        
        with QPainter(self) as painter:
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setPen(Qt.PenStyle.NoPen)

            sliderRect = QRect(0, self.height() // 2 - 2, self.width(), 2)
            
            painter.setBrush(QColor("#d6d6d6"))
            painter.drawRect(sliderRect)

            trackWidth = (self.value() - self.minimum()) / (self.maximum() - self.minimum()) * (self.width() - 16)
            trackRect = QRect(0, self.height() // 2 - 2, trackWidth, 2)
            
            painter.setBrush(QColor("#00a3cc"))
            painter.drawRect(trackRect)

            cursorWidth = 16
            cursorHeight = 16
            cursorRect = QRect(trackWidth, self.height() // 2 - cursorHeight // 2, cursorWidth, cursorHeight)
            
            painter.setBrush(QColor("#00a3cc"))
            painter.drawEllipse(cursorRect)
    
    def getValue(self) -> int:
        if self.f:
            return self.value() / 100
        return self.value()
    
class OptionField(QFrame):
    
    def __init__(self, parameter: str, *args, **kargs) -> None:
        super(OptionField, self).__init__(*args, **kargs)
        
        # widget settings
        self.setFixedHeight(50)
        self.setStyleSheet('background: #c2c2c2')
        
        # widget layout
        if parameter in ['Mutation Rate', 'Crossover Rate', 'Mutation Prob.']:
            self.slider = Slider(min=0, max=100, isFloat=True)
        else:
            if parameter == 'Init Population':
                self.slider = Slider(min=50, max=200, isFloat=False)
            elif parameter == 'Select':
                self.slider = Slider(min=10, max=20, isFloat=False)
        
        font = QFont()
        font.setBold(True)
        font.setFamily('Arial')
        font.setPointSize(10)
        
        title = QLabel()
        title.setFont(font)
        title.setText(parameter)
        
        self.sliderText = QLabel()
        self.sliderText.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.sliderText.setFont(font)
        self.slider.valueChanged.connect(self.updateText)
        self.sliderText.setText(str(self.slider.value()))
        
        textLayout = QHBoxLayout()
        textLayout.setContentsMargins(0,0,0,0)
        textLayout.setSpacing(0)
        textLayout.addWidget(title)
        textLayout.addWidget(self.sliderText)
        
        textFrame = QFrame()
        textFrame.setLayout(textLayout)
        
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(2,2,2,2)
        mainLayout.setSpacing(0)
        mainLayout.addWidget(textFrame)
        mainLayout.addWidget(self.slider)
        self.setLayout(mainLayout)
    
    def updateText(self) -> None:
        self.sliderText.setText(str(self.slider.getValue()))

class OptionFrame(QFrame):
    
    def __init__(self, *args, **kargs) -> None:
        super(OptionFrame, self).__init__(*args, **kargs)
        
        # widget settings
        self.setFixedWidth(250)
        
        # widget layout
        mutationRate = OptionField(parameter='Mutation Rate')
        
        mutationProb = OptionField(parameter='Mutation Prob.')
        
        crossoverRate = OptionField(parameter='Crossover Rate')
        
        population = OptionField(parameter='Init Population')
        
        select = OptionField(parameter='Select')
        
        mainLayout = QVBoxLayout()
        mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        mainLayout.setContentsMargins(20,50,20,50)
        mainLayout.setSpacing(20)
        mainLayout.addWidget(mutationRate)
        mainLayout.addWidget(mutationProb)
        mainLayout.addWidget(crossoverRate)
        mainLayout.addWidget(population)
        mainLayout.addWidget(select)
        self.setLayout(mainLayout)
    
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