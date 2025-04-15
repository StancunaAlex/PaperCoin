from PyQt6.QtCore import QEvent
from PyQt6.QtGui import QAction, QDoubleValidator
from mainWidgets import Widgets
from PyQt6.QtWidgets import QMainWindow
from mainWidgets import RegisterScreen, LoginScreen
from price import fetchPrice

# Initialize main window
class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Papercoin")
        self.setMinimumSize(1280, 800)

# Initialize imports
        self.widgets = Widgets()
        self.setCentralWidget(self.widgets.mainWidget)

# Button functionality
        self.widgets.combobox.currentIndexChanged.connect(self.changeCoin)
        self.widgets.buyButton.clicked.connect(self.price)

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
        if index == 0:
            self.widgets.chart.setHtml(self.widgets.btcCode)
        if index == 1:
            self.widgets.chart.setHtml(self.widgets.ethCode)
        if index == 2:
            self.widgets.chart.setHtml(self.widgets.solCode)

# Add a menu bar
    def bar(self):
        menuBar = self.menuBar()

        editMenu = menuBar.addMenu("Edit")
        settingsMenu = menuBar.addMenu("Settings")

        addBalance = QAction("Add Balance", self)
        addBalance.triggered.connect(self.balanceWindow)

        logout = QAction("Logout", self)
        logout.triggered.connect(self.logout)

        editMenu.addAction(addBalance)
        settingsMenu.addAction(logout)

# Window on menu bar for adding balance
    def balanceWindow(self):
        self.widgets.addBalanceWidget.show()
        self.widgets.balanceButton.clicked.connect(self.balanceLogic)

        validator = QDoubleValidator(self)
        validator.setBottom(0)
        self.widgets.insertBalance.setValidator(validator)

    def balanceLogic(self):
        balanceAmount = self.widgets.insertBalance.text()
        self.widgets.balance.setText(f"Balance: {balanceAmount} $")
        self.widgets.addBalanceWidget.close()

# Logic for logout
    def logout(self):
        self.close()
        self.start = Login()

# Logic for displaying price
    def price(self):
        coinPrice = fetchPrice()
        self.widgets.price.setText(f"Current coin price: {coinPrice} $")


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