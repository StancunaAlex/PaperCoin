from PyQt6.QtWidgets import QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QEvent
from mainWidgets import mainWidgets

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PaperCoin")
        self.setMinimumSize(1280, 800)

        self.widgets = mainWidgets()

        self.widgets.combobox.currentIndexChanged.connect(self.changeCoin)

        self.layout()

    def layout(self):
        self.setCentralWidget(self.widgets.mainWidget)
        self.widgets.mainWidget.setStyleSheet("background-color: #000000;")

        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.widgets.tickerTape, 0, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignTop)
        self.gridLayout.addWidget(self.widgets.chart, 1, 3, 1, 3, alignment=Qt.AlignmentFlag.AlignRight)

        self.comboboxLayout = QVBoxLayout()
        self.comboboxLayout.addWidget(self.widgets.combobox, alignment=Qt.AlignmentFlag.AlignTop)
        self.comboboxLayout.addWidget(self.widgets.balance, alignment=Qt.AlignmentFlag.AlignTop)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.addWidget(self.widgets.buyButton)
        self.buttonsLayout.addWidget(self.widgets.sellButton)

        self.comboboxLayout.addLayout(self.buttonsLayout)
        self.gridLayout.addLayout(self.comboboxLayout, 1, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignTop)

        self.widgets.mainWidget.setLayout(self.gridLayout)

    def resizeEvent(self, event: QEvent):
        windowWidth = self.width()
        windowHeight = self.height()

        self.widgets.tickerTape.setFixedWidth(windowWidth)
        chartWidth = windowWidth // 2
        chartHeight = windowHeight - self.widgets.tickerTape.height()
        self.widgets.chart.setFixedSize(chartWidth, chartHeight)

        super().resizeEvent(event)

    def changeCoin(self, index):
        if index == 0:
            self.widgets.chart.setHtml(self.widgets.btcCode)
        if index == 1:
            self.widgets.chart.setHtml(self.widgets.ethCode)
        if index == 2:
            self.widgets.chart.setHtml(self.widgets.solCode)