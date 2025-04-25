from PyQt6.QtCore import QEvent, QTimer
from PyQt6.QtGui import QAction, QDoubleValidator
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

        self.widgets.slider.setMaximum(0)

        # self.requestPrice = fetchPrice("btc")
        # self.time = QTimer()
        # self.time.timeout.connect(self.updatePrice)
        # self.time.start(1500)

        # self.updatePrice()
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

    def buttons(self):
        self.widgets.combobox.currentIndexChanged.connect(self.changeCoin)
        self.widgets.slider.valueChanged.connect(self.slider)

    def slider(self, value):
        self.widgets.sliderAmount.setText(f'Amount: {value} $')

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

        validator = QDoubleValidator(self)
        validator.setBottom(0)
        self.widgets.insertBalance.setValidator(validator)

    def balanceLogic(self):
        self.balanceAmount = self.widgets.insertBalance.text()
        self.widgets.balance.setText(f"Balance: {self.balanceAmount} $")
        self.widgets.slider.setRange(0, int(self.balanceAmount))
        self.widgets.addBalanceWidget.close()

    def feesSlippage(self):
        self.widgets.feesAndSlippage.show()
        

# Logic for displaying price
    def updatePrice(self):
        index = self.widgets.combobox.currentIndex()
        selectedCoin = "btc" if index == 0 else "eth" if index == 1 else "sol"

        # self.requestPrice = fetchPrice(selectedCoin)

        # if "error" in self.requestPrice:
        #     self.widgets.price.setText(f"Error: {self.requestPrice['error']}")
        # elif "price" in self.requestPrice:
        #     self.widgets.price.setText(f"Current coin price: {self.requestPrice['price']} $")

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