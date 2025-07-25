from PyQt6.QtCore import QEvent, QTimer, QTime
from PyQt6.QtGui import QAction, QDoubleValidator, QRegularExpressionValidator
from PyQt6.QtWidgets import QMainWindow
from mainWidgets import Widgets, RegisterScreen, LoginScreen
from client import fetchPrice
import sqlite3

class MainScreen(QMainWindow):
    def __init__(self, userID):
        super().__init__()
        self.setWindowTitle("Papercoin")
        self.setMinimumSize(1280, 800)

        self.widgets = Widgets()
        self.setCentralWidget(self.widgets.mainWidget)

        self.userID = userID

        self.widgets.buyBox.setMaximum(0)
        self.widgets.sellBox.setMaximum(0)
        self.balanceTotal = 0
        self.balanceAmount = 0
        self.mainAmount = 0
        self.initialCoin = 0
        self.feesPercentage = 0.2
        self.slippagePercentage = 0.05
        self.profit = 0
        self.formattedMainAmount = 0
        self.formattedCoinAmount = 0
        self.coinAmount = 0
        self.investBTC = 0
        self.investETH = 0
        self.investSOL = 0
        self.remainBTC = 0
        self.remainEth = 0
        self.remainSOL = 0
        self.soldBTC = 0
        self.soldETH = 0
        self.soldSOL = 0
        self.sellBoxValue = 0
        self.currentHTML = ""
        self.buyBoxValue = 0
        self.sellBoxValue = 0
        self.spent = 0
        self.statsProfit = 0

        self.requestPrice = fetchPrice("btc")
        self.time = QTimer()
        self.time.timeout.connect(self.updatePrice)
        self.time.start(1500)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTimer)
        self.timer.start(1000)

        self.elapsedTime = QTime(0, 0, 0)

        self.updatePrice()
        self.buttons()
        self.bar()
        self.loadUserStats()

    def resizeEvent(self, event: QEvent):
        windowWidth = self.width()
        windowHeight = self.height()

        self.widgets.tickerTape.setFixedWidth(windowWidth)
        chartWidth = windowWidth // 2
        chartHeight = windowHeight - self.widgets.tickerTape.height()
        self.widgets.chart.setFixedSize(chartWidth, chartHeight)

        super().resizeEvent(event)

    def buttons(self):
        self.widgets.combobox.currentIndexChanged.connect(self.changeCoin)
        self.widgets.balanceButton.clicked.connect(self.balanceLogic)
        self.widgets.feesButton.clicked.connect(self.feesLogic)
        self.widgets.buyBox.valueChanged.connect(self.buyBox)
        self.widgets.sellBox.valueChanged.connect(self.sellBox)
        self.widgets.buyButton.clicked.connect(self.buy)
        self.widgets.sellButton.clicked.connect(self.sell)
        self.widgets.statsReset.clicked.connect(self.resetStats)

        buttons = [
        self.widgets.firstBuyButton, self.widgets.secondBuyButton,
        self.widgets.thirdBuyButton, self.widgets.fourthBuyButton,
        self.widgets.firstSellButton, self.widgets.secondSellButton,
        self.widgets.thirdSellButton, self.widgets.fourthSellButton
]
        for btn in buttons:
            btn.clicked.connect(self.setPercentage)

    def loadUserStats(self):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stats WHERE userID=?", (self.userID,))
        row = cursor.fetchone()

        if row:
            (_, self.mainAmount, self.investBTC, self.soldBTC, self.remainBTC,
            self.investETH, self.soldETH, self.remainEth,
            self.investSOL, self.soldSOL, self.remainSOL, self.balanceTotal,
            self.statsProfit, self.spent, timeSpent, self.coinAmount) = row

            self.elapsedTime = QTime(0, 0, 0).addSecs(timeSpent)
            
            self.widgets.statsSpent.setText(f"Money Spent \n{round(self.spent, 2)} $")
            self.widgets.statsWin.setText(f"Winnings\n{round(self.statsProfit, 2)} $")
            self.widgets.statsCurrBal.setText(f"Current Balance\n{round(self.mainAmount, 2)} $")
            self.widgets.balance.setText(f"Balance: {round(self.mainAmount, 2)} $")
            self.widgets.statsBalance.setText(f"Balance Added\n{round(self.balanceTotal)} $")
            self.widgets.buyBox.setRange(0, round(self.mainAmount, 2))
            self.widgets.sellBox.setRange(0, round(self.coinAmount, 6))
            self.widgets.statsBtc.setText(f"BTC Bought\n{self.investBTC}")
            self.widgets.soldStatsBtc.setText(f"BTC Sold\n{self.soldBTC}")
            self.widgets.remainStatsBtc.setText(f"BTC Remaining\n{self.remainBTC}")
            self.widgets.statsEth.setText(f"ETH Bought\n{self.investETH}")
            self.widgets.soldStatsEth.setText(f"ETH Sold\n{self.soldETH}")
            self.widgets.remainStatsEth.setText(f"ETH Remaining\n{self.remainEth}")
            self.widgets.statsSol.setText(f"SOL Bought\n{self.investSOL}")
            self.widgets.soldStatsSol.setText(f"SOL Sold\n{self.soldSOL}")
            self.widgets.remainStatsSol.setText(f"SOL Remaining\n{self.remainSOL}")
        else:
            cursor.execute("""
                INSERT INTO stats (
                userID, mainAmount, investBTC, soldBTC, remainBTC,
                investETH, soldETH, remainETH,
                investSOL, soldSOL, remainSOL,
                balanceTotal, statsProfit, spent, timeSpent, coinAmount
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (self.userID, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0)
            )

            conn.commit()
            conn.close()

    def buyBox(self, value):
        self.widgets.buyBoxAmount.setText(f'Amount: {value} $')
        self.buyBoxValue = float(value)

    def sellBox(self, value):
        self.widgets.sellBoxAmount.setText(f'Amount: {value} {self.selectedCoin.upper()}')
        self.sellBoxValue = float(value)

    def changeCoin(self, index):
        if index == 0:
            self.selectedCoin = "btc"
            self.initialCoin = self.remainBTC
            self.widgets.investedBtn.setText(f"Invested\n{round(self.investBTC, 6)}")
            self.widgets.soldBtn.setText(f"Sold\n{round(self.soldBTC, 6)}")
            self.widgets.remainBtn.setText(f"Remaining\n{round(self.remainBTC, 6)}")
            self.widgets.invested.setText(f"Invested: {self.investBTC} {self.selectedCoin.upper()}")
            self.infoBtc()
            self.updatePrice()
            if self.currentHTML != self.widgets.btcCode:
                self.currentHTML = self.widgets.btcCode
                self.widgets.chart.setHtml(self.widgets.btcCode)

        elif index == 1:
            self.selectedCoin = "eth"
            self.initialCoin = self.remainEth
            self.widgets.investedBtn.setText(f"Invested\n{round(self.investETH, 6)}")
            self.widgets.soldBtn.setText(f"Sold\n{round(self.soldETH, 6)}")
            self.widgets.remainBtn.setText(f"Remaining\n{round(self.remainEth, 6)}")
            self.widgets.invested.setText(f"Invested: {self.investETH} {self.selectedCoin.upper()} ")
            self.infoEth()
            self.updatePrice()
            if self.currentHTML != self.widgets.ethCode:
                self.currentHTML = self.widgets.ethCode
                self.widgets.chart.setHtml(self.widgets.ethCode)

        elif index == 2:
            self.selectedCoin = "sol"
            self.initialCoin = self.remainSOL
            self.widgets.investedBtn.setText(f"Invested\n{round(self.investSOL, 6)}")
            self.widgets.soldBtn.setText(f"Sold\n{round(self.soldSOL, 6)}")
            self.widgets.remainBtn.setText(f"Remaining\n{round(self.remainSOL, 6)}")
            self.widgets.invested.setText(f"Invested: {self.investSOL} {self.selectedCoin.upper()}")
            self.infoSol()
            self.updatePrice()
            if self.currentHTML != self.widgets.solCode:
                self.currentHTML = self.widgets.solCode
                self.widgets.chart.setHtml(self.widgets.solCode)


    def bar(self):
        menuBar = self.menuBar()

        editMenu = menuBar.addMenu("Edit")
        settingsMenu = menuBar.addMenu("Settings")
        viewMenu = menuBar.addMenu("View")

        addBalance = QAction("Add Balance", self)
        addBalance.triggered.connect(self.balanceWindow)

        logout = QAction("Logout", self)
        logout.triggered.connect(self.logout)

        fees = QAction("Fees and Slippage", self)
        fees.triggered.connect(self.feesSlippage)

        stats = QAction("Statistics", self)
        stats.triggered.connect(self.stats)

        editMenu.addAction(addBalance)
        editMenu.addAction(fees)
        settingsMenu.addAction(logout)
        viewMenu.addAction(stats)

    def balanceWindow(self):
        self.widgets.addBalanceWidget.show()
        balanceValidator = QDoubleValidator(self)
        balanceValidator.setBottom(0)
        self.widgets.insertBalance.setValidator(balanceValidator)

    def balanceLogic(self):
        self.balanceAmount = float(self.widgets.insertBalance.text())
        self.mainAmount = self.mainAmount + self.balanceAmount
        self.balanceTotal += self.balanceAmount
        self.widgets.balance.setText(f"Balance: {self.mainAmount} $")
        self.widgets.buyBox.setRange(0, self.mainAmount)
        self.widgets.statsCurrBal.setText(f"Current Balance\n{round(self.mainAmount, 2)} $")
        self.widgets.statsBalance.setText(f"Balance Added\n{round(self.balanceTotal, 2)} $")
        self.widgets.insertBalance.clear()
        self.widgets.addBalanceWidget.close()
        self.setPercentage()
        self.saveUserStats()

    def feesSlippage(self):
        self.widgets.feesWidget.show()
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

    def stats(self):
        self.widgets.statsWid.show()

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
                self.adjustedPrice = self.coinPrice * (1 + self.slippage)
                self.coinAmount = self.buyBoxValue * (1 - self.fees) / self.adjustedPrice
                self.initialCoin = self.initialCoin + self.coinAmount
                self.formattedCoinAmount = round(self.initialCoin, 6)

                if self.selectedCoin == 'btc':
                    self.investBTC += round(self.coinAmount ,6)
                    self.remainBTC += round(self.coinAmount ,6)
                elif self.selectedCoin == 'eth':
                    self.investETH += round(self.coinAmount ,6)
                    self.remainEth += round(self.coinAmount ,6)
                elif self.selectedCoin == 'sol':
                    self.investSOL += round(self.coinAmount ,6)
                    self.remainSOL += round(self.coinAmount ,6)

                self.mainAmount = self.mainAmount - self.buyBoxValue
                self.formattedMainAmount = round(self.mainAmount, 2)
                self.widgets.balance.setText(f"Balance: {self.formattedMainAmount} $")
                self.widgets.buyBox.setRange(0, self.formattedMainAmount)
                self.widgets.sellBox.setRange(0, float(self.formattedCoinAmount))
                if abs(self.mainAmount) < 1e-6:
                    self.mainAmount = 0.0

                self.spent += self.buyBoxValue
                self.widgets.statsSpent.setText(f"Money Spent \n{round(self.spent, 2)} $")

            for btn in self.percentageButtons:
                btn.setStyleSheet(self.widgets.buyButtonsStyle)

            self.statsProfit -= self.buyBoxValue
            self.widgets.statsWin.setText(f"Winnings\n{round(self.statsProfit, 2)} $")
            self.widgets.buyBox.clear()
            self.widgets.sellBox.clear()
            self.changeCoin(self.widgets.combobox.currentIndex())
            self.widgets.statsCurrBal.setText(f"Current Balance\n{round(self.mainAmount, 2)} $")

            self.saveUserStats()

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
                self.coinPrice = self.requestPrice['price']
                self.fees = self.feesPercentage / 100
                self.slippage = self.slippagePercentage / 100

                self.initialCoin = self.initialCoin - self.sellBoxValue
                if abs(self.initialCoin) < 1e-6:
                    self.initialCoin = 0.0
                self.formattedCoinAmount = round(self.initialCoin, 6)

                if self.selectedCoin == 'btc':
                    self.soldBTC += self.sellBoxValue
                    self.remainBTC -= self.sellBoxValue
                    self.widgets.sellBoxAmount.setText(f"Amount: {self.remainBTC}")
                elif self.selectedCoin == 'eth':
                    self.soldETH += self.sellBoxValue
                    self.remainEth -= self.sellBoxValue
                    self.widgets.sellBoxAmount.setText(f"Amount: {self.remainEth}")
                elif self.selectedCoin == 'sol':
                    self.soldSOL += self.sellBoxValue
                    self.remainSOL -= self.sellBoxValue
                    self.widgets.sellBoxAmount.setText(f"Amount: {self.remainSOL}")

                self.adjustedPrice = self.coinPrice * (1 - self.slippage)
                self.rawProfit = self.adjustedPrice * self.sellBoxValue
                self.finalProfit = self.rawProfit * (1 - self.fees)

                self.mainAmount = self.mainAmount + self.finalProfit
                if abs(self.mainAmount) < 1e-6:
                    self.mainAmount = 0.0
                self.formattedMainAmount = round(self.mainAmount, 2)
                self.widgets.balance.setText(f"Balance: {self.formattedMainAmount} $")
                self.widgets.buyBox.setRange(0, self.formattedMainAmount)

            for btn in self.percentageButtons:
                btn.setStyleSheet(self.widgets.buyButtonsStyle)

            self.statsProfit += self.finalProfit
            self.widgets.statsWin.setText(f"Winnings\n{round(self.statsProfit, 2)} $")
            self.widgets.sellBox.clear()
            self.widgets.buyBox.clear()
            self.changeCoin(self.widgets.combobox.currentIndex())
            self.widgets.statsCurrBal.setText(f"Current Balance\n{round(self.mainAmount, 2)} $")

            self.saveUserStats()

    def setPercentage(self):
        buttonClick = self.sender()

        self.percentageButtons = [
                   self.widgets.firstBuyButton, self.widgets.secondBuyButton,
                   self.widgets.thirdBuyButton, self.widgets.fourthBuyButton,
                   self.widgets.firstSellButton, self.widgets.secondSellButton,
                   self.widgets.thirdSellButton, self.widgets.fourthSellButton
                   ]

        for btn in self.percentageButtons:
            btn.setStyleSheet(self.widgets.buyButtonsStyle)

            if buttonClick in self.percentageButtons[0:4]:
                buttonClick.setStyleSheet(self.widgets.activeBuyStyle)
            elif buttonClick in self.percentageButtons[4:]:
                buttonClick.setStyleSheet(self.widgets.activeSellStyle)

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

    def updatePrice(self):
        index = self.widgets.combobox.currentIndex()
        self.selectedCoin = "btc" if index == 0 else "eth" if index == 1 else "sol"

        self.requestPrice = fetchPrice(self.selectedCoin)

        if "error" in self.requestPrice:
            self.widgets.price.setText(f"Error: Too many requests!")
        elif "price" in self.requestPrice:
            self.widgets.price.setText(f"Current coin price: {self.requestPrice['price']} $")

    def infoBtc(self):
            self.selectedCoin = "btc"
            self.widgets.investedBtn.setText(f"Invested\n{round(self.investBTC, 6)}")
            self.widgets.soldBtn.setText(f"Sold\n{round(self.soldBTC, 6)}")
            self.widgets.remainBtn.setText(f"Remaining\n{round(self.remainBTC, 6)}")

            self.widgets.statsBtc.setText(f"BTC Bought\n{round(self.investBTC, 6)}")
            self.widgets.remainStatsBtc.setText(f"BTC Remaining\n{round(self.remainBTC, 6)}")
            self.widgets.soldStatsBtc.setText(f"BTC Sold\n{round(self.soldBTC, 6)}")

    def infoEth(self):
            self.selectedCoin = "eth"
            self.widgets.investedBtn.setText(f"Invested\n{round(self.investETH, 6)}")
            self.widgets.soldBtn.setText(f"Sold\n{round(self.soldETH, 6)}")
            self.widgets.remainBtn.setText(f"Remaining\n{round(self.remainEth, 6)}")

            self.widgets.statsEth.setText(f"ETH Bought\n{round(self.investETH, 6)}")
            self.widgets.remainStatsEth.setText(f"ETH Remaining\n{round(self.remainEth, 6)}")
            self.widgets.soldStatsEth.setText(f"ETH Sold\n{round(self.soldETH, 6)}")

    def infoSol(self):
            self.selectedCoin = "sol"
            self.widgets.investedBtn.setText(f"Invested\n{round(self.investSOL, 6)}")
            self.widgets.soldBtn.setText(f"Sold\n{round(self.soldSOL, 6)}")
            self.widgets.remainBtn.setText(f"Remaining\n{round(self.remainSOL, 6)}")

            self.widgets.statsSol.setText(f"SOL Bought\n{round(self.investSOL, 6)}")
            self.widgets.remainStatsSol.setText(f"SOL Remaining\n{round(self.remainSOL, 6)}")
            self.widgets.soldStatsSol.setText(f"SOL Sold\n{round(self.soldSOL, 6)}")

    def resetStats(self):
        self.widgets.statsBtc.setText("BTC Bought\n-")
        self.widgets.statsEth.setText("ETH Bought\n-")
        self.widgets.statsSol.setText("SOL Bought\n-")
        self.widgets.remainStatsBtc.setText("BTC Remaining\n-")
        self.widgets.remainStatsEth.setText("ETH Remaining\n-")
        self.widgets.remainStatsSol.setText("SOL Remaining\n-")
        self.widgets.soldStatsBtc.setText("BTC Sold\n-")
        self.widgets.soldStatsEth.setText("ETH Sold\n-")
        self.widgets.soldStatsSol.setText("SOL Sold\n-")
        self.widgets.statsCurrBal.setText("Current Balance\n-")
        self.widgets.statsBalance.setText("Balance Added\n-")
        self.widgets.statsSpent.setText("Money Spent\n-")
        self.widgets.statsWin.setText("Winnings\n-")
        self.widgets.timeSpent.setText("Time Spent\n00:00:00")
        self.elapsedTime = QTime(0, 0, 0)

        self.saveUserStats()

    def updateTimer(self):
        self.elapsedTime = self.elapsedTime.addSecs(1)
        self.widgets.timeSpent.setText(f"Time Spent\n{self.elapsedTime.toString('hh:mm:ss')}")

    def saveUserStats(self):
        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE stats 
            SET mainAmount = ?, investBTC = ?, soldBTC = ?, remainBTC = ?, 
                investETH = ?, soldETH = ?, remainETH = ?, investSOL = ?, 
                soldSOL = ?, remainSOL = ?, balanceTotal = ?, statsProfit = ?, 
                spent = ?, timeSpent = ?, coinAmount = ?
            WHERE userID = ?""", 
            (self.mainAmount, self.investBTC, self.soldBTC, self.remainBTC, 
             self.investETH, self.soldETH, self.remainEth, self.investSOL, 
             self.soldSOL, self.remainSOL, self.balanceTotal, self.statsProfit, 
             self.spent, self.elapsedTime.second(), self.coinAmount, self.userID))
            conn.commit()
    
    def logout(self):
        self.close()
        self.start = Login()

class Login():
    def __init__(self):
        self.loginWindow = LoginScreen()
        self.registerWindow = RegisterScreen()
        self.widgets = Widgets()
        self.currentUserId = None

        self.loginWindow.loginButton.clicked.connect(self.loginUser)
        self.loginWindow.registerButton.clicked.connect(self.showRegisterWindow)
        self.registerWindow.backButton.clicked.connect(self.showLoginWindow)
        self.registerWindow.registerBtn.clicked.connect(self.regLogic)

        self.loginWindow.show()

    def showMainWindow(self):
        self.mainWindow.show()
        self.loginWindow.hide()

    def showRegisterWindow(self):
        self.registerWindow.show()
        self.loginWindow.hide()

    def showLoginWindow(self):
        self.registerWindow.hide()
        self.loginWindow.show()

    def regLogic(self):
        username = self.registerWindow.usernameInput.text()
        password = self.registerWindow.passwordInput.text()
        reentered_password = self.registerWindow.reenterPassword.text()

        if password != reentered_password:
            self.widgets.loginError.setText("Passwords do not match")
            self.widgets.loginError.exec()
            
        if not username or not password:
            self.widgets.loginError.setText("All fields are required")
            self.widgets.loginError.exec()

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        try:
            cursor.execute('''
                INSERT INTO users (username, password)
                VALUES (?, ?)
            ''', (username, password))
            conn.commit()
            self.currentUserId = cursor.lastrowid
            self.mainWindow = MainScreen(userID=self.currentUserId)
            self.mainWindow.show()
            self.registerWindow.hide()
        except sqlite3.IntegrityError:
            self.widgets.loginError.setText("This username already exists")
            self.widgets.loginError.exec()
        finally:
            conn.close()

    def loginUser(self):
        username = self.loginWindow.usernameInput.text()
        password = self.loginWindow.passwordInput.text()

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        if result:
            self.currentUserId = result[0]
            self.mainWindow = MainScreen(userID=self.currentUserId)
            self.mainWindow.show()
            self.loginWindow.close()
        else:
            self.widgets.loginError.setText("Incorect username or password")
            self.widgets.loginError.exec()