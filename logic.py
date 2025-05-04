from PyQt6.QtCore import QEvent, QTimer
from PyQt6.QtGui import QAction, QDoubleValidator, QRegularExpressionValidator
from PyQt6.QtWidgets import QMainWindow
from mainWidgets import Widgets, RegisterScreen, LoginScreen
from client import fetchPrice

# Initialize main window
class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Papercoin")
        self.setMinimumSize(1280, 800)

# Initialize imports
        self.widgets = Widgets()
        self.setCentralWidget(self.widgets.mainWidget)

# Set variables
        self.widgets.buyBox.setMaximum(0)
        self.widgets.sellBox.setMaximum(0)
        self.balanceAmount = 0
        self.mainAmount = 0
        self.initialCoin = 0
        self.feesPercentage = 0.2
        self.slippagePercentage = 0.05
        self.profit = 0
        self.formattedMainAmount = 0
        self.formattedCoinAmount = 0

        self.requestPrice = fetchPrice("btc")
        self.time = QTimer()
        self.time.timeout.connect(self.updatePrice)
        self.time.start(1500)

        self.updatePrice()
        self.buttons()
        self.bar()

# Resize the right chart
    def resizeEvent(self, event: QEvent):
        windowWidth = self.width()
        windowHeight = self.height()

        self.widgets.tickerTape.setFixedWidth(windowWidth)
        chartWidth = windowWidth // 2
        chartHeight = windowHeight - self.widgets.tickerTape.height()
        self.widgets.chart.setFixedSize(chartWidth, chartHeight)

        super().resizeEvent(event)

# Change the coin using the combobox
    def changeCoin(self, index):
        index == 0

        if index == 0:
            self.widgets.chart.setHtml(self.widgets.btcCode)
            self.updatePrice()

        if index == 1:
            self.widgets.chart.setHtml(self.widgets.ethCode)
            self.updatePrice()

        if index == 2:
            self.widgets.chart.setHtml(self.widgets.solCode)
            self.updatePrice()

# Button logic
    def buttons(self):
        self.widgets.combobox.currentIndexChanged.connect(self.changeCoin)
        self.widgets.buyBox.valueChanged.connect(self.buyBox)
        self.widgets.sellBox.valueChanged.connect(self.sellBox)
        self.widgets.buyButton.clicked.connect(self.buy)
        self.widgets.sellButton.clicked.connect(self.sell)

        buttons = [
        self.widgets.firstBuyButton,
        self.widgets.secondBuyButton,
        self.widgets.thirdBuyButton,
        self.widgets.fourthBuyButton,
        self.widgets.firstSellButton,
        self.widgets.secondSellButton,
        self.widgets.thirdSellButton,
        self.widgets.fourthSellButton
]
        for button in buttons:
            button.clicked.connect(self.setPercentage)

# DoubleBox logic
    def buyBox(self, value):
        self.widgets.buyBoxAmount.setText(f'Amount: {value} $')
        self.buyBoxValue = float(value)

    def sellBox(self, value):
        self.widgets.sellBoxAmount.setText(f'Amount: {value} {self.selectedCoin}')
        self.sellBoxValue = float(value)

# Add a menu bar
    def bar(self):
        menuBar = self.menuBar()

        editMenu = menuBar.addMenu("Edit")
        settingsMenu = menuBar.addMenu("Settings")

        addBalance = QAction("Add Balance", self)
        addBalance.triggered.connect(self.balanceWindow)

        logout = QAction("Logout", self)
        logout.triggered.connect(self.logout)

        fees = QAction("Fees and Slippage", self)
        fees.triggered.connect(self.feesSlippage)

        editMenu.addAction(addBalance)
        settingsMenu.addAction(fees)
        settingsMenu.addAction(logout)

# Window on menu bar for adding balance
    def balanceWindow(self):
        self.widgets.addBalanceWidget.show()
        self.widgets.balanceButton.clicked.connect(self.balanceLogic)

        balanceValidator = QDoubleValidator(self)
        balanceValidator.setBottom(0)
        self.widgets.insertBalance.setValidator(balanceValidator)

    def balanceLogic(self):
        self.balanceAmount = float(self.widgets.insertBalance.text())
        self.mainAmount = self.mainAmount + self.balanceAmount
        self.widgets.balance.setText(f"Balance: {self.mainAmount} $")
        self.widgets.buyBox.setRange(0, self.mainAmount)
        self.widgets.addBalanceWidget.close()
        self.setPercentage()

# Fees and slippage logic
    def feesSlippage(self):
        self.widgets.feesWidget.show()
        self.widgets.feesButton.clicked.connect(self.feesLogic)

        feesValidator = QRegularExpressionValidator()
        self.widgets.insertFees.setValidator(feesValidator)
        self.widgets.insertSlippage.setValidator(feesValidator)

    def feesLogic(self):
        self.feesPercentage = float(self.widgets.insertFees.text())
        self.slippagePercentage = float(self.widgets.insertSlippage.text())
        if self.feesPercentage < 0 or self.slippagePercentage < 0:
            self.widgets.errorText.setStyleSheet("color :#000000;")
            self.widgets.errorText.setText("Cannot use negative numbers")
            self.widgets.errorWidget.show()
        else:
            self.widgets.feesWidget.close()

# Buy button logic
    def buy(self):
        if self.mainAmount <= 0:
            self.widgets.error.setText("Insufficient balance!")
            self.widgets.buyBox.clear()

        elif self.buyBoxValue == 0:
            self.widgets.error.setText("No buy value selected!")

        else:
            self.widgets.error.setText("")
            if round(self.mainAmount, 2) < round(self.buyBoxValue, 2):
                self.widgets.error.setText("Insufficient balance!")

            else:
                self.fees = self.feesPercentage / 100
                self.slippage = self.slippagePercentage / 100

                self.coinPrice = self.requestPrice['price']
                adjustedPrice = self.coinPrice * (1 + self.slippage)
                self.coinAmount = self.buyBoxValue * (1 - self.fees) / adjustedPrice
                self.initialCoin = self.initialCoin + self.coinAmount
                self.formattedCoinAmount = round(self.initialCoin, 6)
                self.widgets.invested.setText(f"Invested: {self.formattedCoinAmount} {self.selectedCoin}")

                self.mainAmount = self.mainAmount - self.buyBoxValue
                self.formattedMainAmount = round(self.mainAmount, 2)
                self.widgets.balance.setText(f"Balance: {self.formattedMainAmount} $")
                self.widgets.buyBox.setRange(0, self.formattedMainAmount)
                self.widgets.sellBox.setRange(0, float(self.formattedCoinAmount))
                if abs(self.mainAmount) < 1e-6:
                    self.mainAmount = 0.0

            for btn in self.percentageButtons:
                btn.setStyleSheet(self.widgets.buyButtonsStyle)

            self.widgets.buyBox.clear()

# Sell button logic
    def sell(self):
        if self.initialCoin <= 0:
            self.widgets.error.setText(f"Not enough {self.selectedCoin.upper()}!")
            self.widgets.sellBox.clear()

        elif self.sellBoxValue == 0:
            self.widgets.error.setText("No sell value selected!")

        else:
            self.widgets.error.setText("")
            if round(self.initialCoin, 6) < round(self.sellBoxValue, 6):
                self.widgets.error.setText(f"Not enought {self.selectedCoin.upper()}!")
            else:
                self.initialCoin = self.initialCoin - self.sellBoxValue
                if abs(self.initialCoin) < 1e-6:
                    self.initialCoin = 0.0
                self.formattedCoinAmount = round(self.initialCoin, 6)
                self.widgets.invested.setText(f"Invested: {self.formattedCoinAmount} {self.selectedCoin}")

                adjustedPrice = self.coinPrice * (1 - self.slippage)
                self.rawProfit = adjustedPrice * self.sellBoxValue
                self.finalProfit = self.rawProfit * (1 - self.fees)

                self.mainAmount = self.mainAmount + self.finalProfit
                if abs(self.mainAmount) < 1e-6:
                    self.mainAmount = 0.0
                self.formattedMainAmount = round(self.mainAmount, 2)
                self.widgets.balance.setText(f"Balance: {self.formattedMainAmount} $")
                self.widgets.buyBox.setRange(0, self.formattedMainAmount)

            for btn in self.percentageButtons:
                btn.setStyleSheet(self.widgets.buyButtonsStyle)

            self.widgets.sellBox.clear()

    def setPercentage(self):
        buttonClick = self.sender()

        self.percentageButtons = [self.widgets.firstBuyButton,
                   self.widgets.secondBuyButton,
                   self.widgets.thirdBuyButton,
                   self.widgets.fourthBuyButton,
                   self.widgets.firstSellButton,
                   self.widgets.secondSellButton,
                   self.widgets.thirdSellButton,
                   self.widgets.fourthSellButton
                   ]

        for btn in self.percentageButtons:
            btn.setStyleSheet(self.widgets.buyButtonsStyle)

            buttonClick.setStyleSheet(self.widgets.activeBuyStyle)

        if buttonClick == self.widgets.firstBuyButton:
            firstPercentageAmount = (25 / 100) * self.mainAmount
            self.widgets.buyBox.setValue(round(firstPercentageAmount, 2))

        elif buttonClick == self.widgets.secondBuyButton:
            secondPercentageAmount = (50 / 100) * self.mainAmount
            self.widgets.buyBox.setValue(round(secondPercentageAmount, 2))

        elif buttonClick == self.widgets.thirdBuyButton:
            thirdPercentageAmount = (75 / 100) * self.mainAmount
            self.widgets.buyBox.setValue(round(thirdPercentageAmount, 2))

        elif buttonClick == self.widgets.fourthBuyButton:
            fourthPercentageAmount = min(self.mainAmount, round(self.mainAmount, 2))
            self.widgets.buyBox.setValue(fourthPercentageAmount)

        elif buttonClick == self.widgets.firstSellButton:
            firstSellPercentageAmount = (25 / 100) * self.initialCoin
            self.widgets.sellBox.setValue(round(firstSellPercentageAmount, 6))

        elif buttonClick == self.widgets.secondSellButton:
            secondSellPercentageAmount = (50 / 100) * self.initialCoin
            self.widgets.sellBox.setValue(round(secondSellPercentageAmount, 6))

        elif buttonClick == self.widgets.thirdSellButton:
            thirdSellPercentageAmount = (75 / 100) * self.initialCoin
            self.widgets.sellBox.setValue(round(thirdSellPercentageAmount, 6))

        elif buttonClick == self.widgets.fourthSellButton:
            fourthSellPercentageAmount = min(self.initialCoin, round(self.initialCoin, 6))
            self.widgets.sellBox.setValue(fourthSellPercentageAmount)

# Logic for displaying price
    def updatePrice(self):
        index = self.widgets.combobox.currentIndex()
        self.selectedCoin = "btc" if index == 0 else "eth" if index == 1 else "sol"

        self.requestPrice = fetchPrice(self.selectedCoin)

        if "error" in self.requestPrice:
            self.widgets.price.setText(f"Error: Too many requests!")
        elif "price" in self.requestPrice:
            self.widgets.price.setText(f"Current coin price: {self.requestPrice['price']} $")

# Logic for logout
    def logout(self):
        self.close()
        self.start = Login()

# Initialize login
class Login():
    def __init__(self):
        self.mainWindow = MainScreen()
        self.loginWindow = LoginScreen()
        self.registerWindow = RegisterScreen()

        self.loginWindow.show()
        self.logic()

    def logic(self):
        self.loginWindow.registerButton.clicked.connect(self.showRegisterWindow)
        self.loginWindow.loginButton.clicked.connect(self.showMainWindow)
        self.registerWindow.backButton.clicked.connect(self.showLoginWindow)

    def showRegisterWindow(self):
        self.registerWindow.show()
        self.loginWindow.hide()

    def showMainWindow(self):
        self.mainWindow.show()
        self.loginWindow.hide()

    def showLoginWindow(self):
        self.registerWindow.hide()
        self.loginWindow.show()