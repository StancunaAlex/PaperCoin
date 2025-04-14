from PyQt6.QtCore import QEvent
from PyQt6.QtGui import QAction, QDoubleValidator
from mainWidgets import mainWidgets
from PyQt6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PaperCoin")
        self.setMinimumSize(1280, 800)

        self.widgets = mainWidgets()
        self.setCentralWidget(self.widgets.mainWidget)

        self.widgets.combobox.currentIndexChanged.connect(self.changeCoin)

        self.bar()
        self.widgets.layout()

    def bar(self):
        menuBar = self.menuBar()
        editMenu = menuBar.addMenu("File")

        addBalance = QAction("Add Balance", self)
        addBalance.triggered.connect(self.balanceWindow)

        editMenu.addAction(addBalance)

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

    def balanceWindow(self):
        self.widgets.addBalanceWidget.show()
        self.widgets.balanceButton.clicked.connect(self.balanceLogic)

        validator = QDoubleValidator(self)
        validator.setBottom(0)
        self.widgets.insertBalance.setValidator(validator)

    def balanceLogic(self):
        balanceAmount = self.widgets.insertBalance.text()
        self.widgets.balance.setText(f"Balance: {balanceAmount} $")
        self.widgets.addBalanceWidget.hide()