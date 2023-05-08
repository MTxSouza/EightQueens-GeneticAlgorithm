# imports
from itertools import product
from utils.widgets import *
from typing import Union


class Button(QToolButton):
    
    def __init__(self, *args, **kargs):
        super(Button, self).__init__(*args, **kargs)
        
        # widget settings
        self.setFixedSize(QSize(150, 30))
        
        # widget layout
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setColor(QColor('#00a3cc'))
        self.shadow.setOffset(0)
        self.setGraphicsEffect(self.shadow)
        
        font = QFont()
        font.setBold(True)
        font.setFamily('Arial')
        font.setPointSize(10)
        self.setFont(font)
    
    def paintEvent(self, arg__1: QPaintEvent) -> None:
        
        with QPainter(self) as painter:
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            
            pen = QPen()
            if self.underMouse():
                self.setCursor(Qt.CursorShape.PointingHandCursor)
                pen.setWidth(2)
                if self.isDown():
                    painter.setBrush(QColor('#b9b6b6'))
                    self.shadow.setBlurRadius(5)
                else:
                    painter.setBrush(QColor('#c2c2c2'))
                    self.shadow.setBlurRadius(15)
                pen.setColor(QColor('#05c1ff'))
            else:
                self.setCursor(Qt.CursorShape.ArrowCursor)
                pen.setWidth(1)
                pen.setColor(QColor('#474747'))
                self.shadow.setBlurRadius(0)
                painter.setBrush(QColor('#c2c2c2'))
            painter.setPen(pen)
            
            rect = self.rect()
            painter.drawRoundedRect(rect, 15, 15)
            
            pen.setColor(QColor('#474747'))
            painter.setPen(pen)
            
            painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, 'Run')
            
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
            elif parameter == 'Attempts':
                self.slider = Slider(min=100, max=10000, isFloat=False)
        
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
    
    def value(self) -> Union[int, float]:
        return self.slider.getValue()

class OptionFrame(QFrame):
    
    def __init__(self, model: object, *args, **kargs) -> None:
        super(OptionFrame, self).__init__(*args, **kargs)
        
        # widget settings
        self.setFixedWidth(250)
        
        # model
        self.model = model
        
        # widget layout
        self.mutationRate = OptionField(parameter='Mutation Rate')
        self.mutationProb = OptionField(parameter='Mutation Prob.')
        self.crossoverRate = OptionField(parameter='Crossover Rate')
        self.population = OptionField(parameter='Init Population')
        self.select = OptionField(parameter='Select')
        self.attempts = OptionField(parameter='Attempts')
        
        sliderLayout = QVBoxLayout()
        sliderLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        sliderLayout.setContentsMargins(20,50,20,50)
        sliderLayout.setSpacing(20)
        sliderLayout.addWidget(self.mutationRate)
        sliderLayout.addWidget(self.mutationProb)
        sliderLayout.addWidget(self.crossoverRate)
        sliderLayout.addWidget(self.population)
        sliderLayout.addWidget(self.select)
        sliderLayout.addWidget(self.attempts)
        
        sliderFrame = QFrame()
        sliderFrame.setStyleSheet('background: #c2c2c2')
        sliderFrame.setLayout(sliderLayout)
        
        buttonRun = Button()
        buttonRun.clicked.connect(self.run)
        
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(buttonRun)
        
        buttonFrame = QFrame()
        buttonFrame.setStyleSheet('background: #c2c2c2')
        buttonFrame.setLayout(buttonLayout)
        
        mainLayout = QVBoxLayout()
        mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        mainLayout.setContentsMargins(20,50,20,50)
        mainLayout.setSpacing(0)
        mainLayout.addWidget(sliderFrame)
        mainLayout.addWidget(buttonFrame)
        self.setLayout(mainLayout)
    
    def paintEvent(self, arg__1: QPaintEvent) -> None:
        
        with QPainter(self) as painter:
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            
            painter.setBrush(QColor('#c2c2c2'))
            
            rect = self.rect()
            painter.drawRoundedRect(rect, 30, 30)
    
    def run(self) -> None:
        if self.model is not None:
            try:
                self.model.config(
                    crossover_rate = self.crossoverRate.value(),
                    mutation_rate = self.mutationRate.value(), 
                    mutation_p = self.mutationProb.value(), 
                    init_population = self.population.value(), 
                    selection = self.select.value()
                )
            except Exception as error:
                ...
            else:
                pop, gen, check = self.model.run(attempts=self.attempts.value())

class Board(QFrame):
    
    def __init__(self, *args, **kargs) -> None:
        super(Board, self).__init__(*args, **kargs)
        
        # widget settings
        self.setStyleSheet('background: #00a3cc')
        self.setFixedSize(QSize(550,550))
        
        # widget layout
        mainLayout = QGridLayout()
        mainLayout.setContentsMargins(5,5,5,5)
        mainLayout.setSpacing(0)
        
        for (row, col) in product(range(8), range(8)):
            field = QLabel()
            field.setStyleSheet(f'background: {"white" if (row + col) % 2 == 0 else "black"}')
            mainLayout.addWidget(field, row, col)
        
        self.setLayout(mainLayout)
        
class GameFrame(QFrame):
    
    def __init__(self, *args, **kargs) -> None:
        super(GameFrame, self).__init__(*args, **kargs)
        
        # widget layout
        mainLayout = QVBoxLayout()
        mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        mainLayout.setContentsMargins(20,5,20,5)
        
        resultLabel = QLabel()
        resultLabel.setStyleSheet('background: #00a3cc')
        resultLabel.setFixedHeight(30)
        
        boardFrame = Board()
        
        mainLayout.addWidget(resultLabel)
        mainLayout.addWidget(boardFrame)
        self.setLayout(mainLayout)

class MainFrame(QFrame):
    
    def __init__(self, model: object = None, *args, **kargs) -> None:
        super(MainFrame, self).__init__(*args, **kargs)
        
        # widget settings
        self.setStyleSheet('background: #d6d6d6')
        
        # widget layout
        optionsFrame = OptionFrame(model=model)
        
        gameFrame = GameFrame()
        
        mainLayout = QHBoxLayout()
        mainLayout.setContentsMargins(30,50,30,50)
        mainLayout.setSpacing(30)
        mainLayout.addWidget(optionsFrame)
        mainLayout.addWidget(gameFrame)
        self.setLayout(mainLayout)