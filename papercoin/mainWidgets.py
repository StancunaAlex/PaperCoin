from PyQt6.QtCore import Qt
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import (QWidget, QComboBox,
    QPushButton, QLabel,
    QLineEdit, QGridLayout,
    QVBoxLayout, QHBoxLayout,
    QDoubleSpinBox, QMessageBox
)

class Widgets(QWidget):
  def __init__(self):
      super().__init__()

      self.mainWidgets()
      self.mainLayout()

  def mainWidgets(self):
      self.mainWidget = QWidget()
      self.mainWidget.setStyleSheet("background-color: #000000;")

      self.errorWidget = QWidget()
      self.errorWidget.setWindowTitle("Error")

      self.addBalanceWidget = QWidget()
      self.addBalanceWidget.setWindowTitle("Add Balance")
      self.addBalanceWidget.setMaximumSize(200, 96)

      self.feesWidget = QWidget()
      self.feesWidget.setWindowTitle("Settings")
      self.feesWidget.setMaximumSize(200, 116)

      self.statsWid = QWidget()
      self.statsWid.setWindowTitle("Statistics")
      self.statsWid.setStyleSheet("background-color: #000000;")
      self.statsWid.setMinimumSize(800, 400)

      self.chart = QWebEngineView()
      self.tickerTape = QWebEngineView()
      self.tickerTape.setFixedHeight(60)

      self.buyButtonsStyle = """
    QPushButton {
        background-color: #303336;
        color: #BAC7CF;  
    }
"""

      textStyle = "color: #BAC7CF;"

      self.activeBuyStyle = """
    QPushButton {
        background-color: #303336;
        color: #BAC7CF;
        border: 1px solid #0ABF34;     
    }
"""

      self.activeSellStyle = """
    QPushButton {
        background-color: #303336;    
        color: #BAC7CF;
        border: 1px solid #BF0A19;     
    }
"""

      self.infoBtns = """
    QLabel {
        background-color: #000000;    
        color: #BAC7CF;
        border: 1px solid #303336;     
    }
"""

      self.buyButton = QPushButton("Buy")
      self.buyButton.setStyleSheet("background-color: #0ABF34;")
      self.firstBuyButton = QPushButton("25%")
      self.secondBuyButton = QPushButton("50%")
      self.thirdBuyButton = QPushButton("75%")
      self.fourthBuyButton = QPushButton("100%")

      self.sellButton = QPushButton("Sell")
      self.sellButton.setStyleSheet("background-color: #BF0A19")
      self.firstSellButton = QPushButton("25%")
      self.secondSellButton = QPushButton("50%")
      self.thirdSellButton = QPushButton("75%")
      self.fourthSellButton = QPushButton("100%")

      self.statsReset = QPushButton("Reset Statistics")

      percButton = [self.firstBuyButton, self.secondBuyButton, self.thirdBuyButton,
                    self.fourthBuyButton, self.firstSellButton, self.secondSellButton,
                    self.thirdSellButton, self.fourthSellButton, self.statsReset]
      
      for perc in percButton:
        perc.setStyleSheet(self.buyButtonsStyle)

      self.balanceButton = QPushButton("Accept")
      self.feesButton = QPushButton("Accept")

      self.investedBtn = QLabel("Invested\n-")
      self.soldBtn = QLabel("Sold\n-")
      self.remainBtn = QLabel("Reamining\n-")
      self.statsBtc = QLabel("BTC Bought\n-")
      self.statsEth = QLabel("ETH Bought\n-")
      self.statsSol = QLabel("SOL Bought\n-")
      self.remainStatsBtc = QLabel("BTC Remaining\n-")
      self.remainStatsEth = QLabel("ETH Remaining\n-")
      self.remainStatsSol = QLabel("SOL Remaining\n-")
      self.soldStatsBtc = QLabel("BTC Sold\n-")
      self.soldStatsEth = QLabel("ETH Sold\n-")
      self.soldStatsSol = QLabel("SOL Sold\n-")
      self.statsCurrBal = QLabel("Current Balance\n-")
      self.statsBalance = QLabel("Balance Added\n-")
      self.statsSpent = QLabel("Money Spent\n-")
      self.statsWin = QLabel("Winnings\n-")
      self.timeSpent = QLabel("Time Spent\n00:00:00")

      info = [self.investedBtn, self.soldBtn, self.remainBtn,
              self.statsBtc, self.statsEth, self.statsSol, self.remainStatsBtc,
              self.remainStatsEth, self.remainStatsSol, self.soldStatsBtc,
              self.soldStatsEth, self.soldStatsSol, self.statsBalance, 
              self.statsSpent, self.statsWin, self.statsCurrBal, self.timeSpent]

      for btn in info:
        btn.setStyleSheet(self.infoBtns)
        btn.setAlignment(Qt.AlignmentFlag.AlignCenter)

      self.combobox = QComboBox()
      self.combobox.addItems(['Bitcoin', 'Ethereum', 'Solana'])
      self.combobox.setStyleSheet("""background-color: #303336; color: #BAC7CF;""")

      self.balance = QLabel("Balance: 0 $")
      self.price = QLabel("Price:")
      self.invested = QLabel("Invested: 0")
      self.buyBoxAmount = QLabel("Amount: 0 $")
      self.sellBoxAmount = QLabel("Amount: 0")
      self.error = QLabel()
      self.errorText = QLabel()
      
      self.insertFeesText = QLabel("Default is set to 0.2 for fees and 0.05 for slippage")
      self.addBalance = QLabel("Add the balance amount:")
      self.fees = QLabel("Adjust fees amount:")
      self.fees.setToolTip("Fees are small fixed percentage charged for each buy or sell.")
      self.slippage = QLabel("Adjust slippage amount:")
      self.slippage.setToolTip("Slippage is the difference between the expected price"
      " and the actual price when a trade happens.")

      self.insertBalance = QLineEdit()
      self.insertFees = QLineEdit()
      self.insertSlippage = QLineEdit()

      self.buyBox = QDoubleSpinBox()
      self.buyBox.clear()

      self.sellBox = QDoubleSpinBox()
      self.sellBox.setDecimals(8)
      self.sellBox.clear()

      text = [self.balance, self.buyBoxAmount, self.price, self.error, self.invested,
              self.sellBoxAmount, self.buyBox, self.sellBox]

      for txt in text:
        txt.setStyleSheet(textStyle)

      self.loginError = QMessageBox()
      self.loginError.setIcon(QMessageBox.Icon.Critical)
      self.loginError.setWindowTitle("Error")
      self.loginError.setText("")
      self.loginError.setStandardButtons(QMessageBox.StandardButton.Ok)

      tickerTape = '''
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>
  {
  "symbols": [
    {
      "proName": "BITSTAMP:BTCUSD",
      "title": "Bitcoin"
    },
    {
      "proName": "BITSTAMP:ETHUSD",
      "title": "Ethereum"
    },
    {
      "description": "Solana",
      "proName": "COINBASE:SOLUSD"
    }
  ],
  "showSymbolLogo": true,
  "isTransparent": false,
  "displayMode": "adaptive",
  "colorTheme": "dark",
  "locale": "en"
}
  </script>
</div>
      '''

      self.btcCode = '''
        <div class="tradingview-widget-container" style="height:100%;width:100%">
  <div class="tradingview-widget-container__widget" style="height:calc(100% - 32px);width:100%"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
  {
  "autosize": true,
  "symbol": "BITSTAMP:BTCUSD",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "hide_side_toolbar": false,
  "allow_symbol_change": true,
  "support_host": "https://www.tradingview.com"
}
  </script>
</div>'''

      self.ethCode = '''<div class="tradingview-widget-container" style="height:100%;width:100%">
  <div class="tradingview-widget-container__widget" style="height:calc(100% - 32px);width:100%"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
  {
  "autosize": true,
  "symbol": "BITSTAMP:ETHUSD",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "hide_side_toolbar": false,
  "allow_symbol_change": true,
  "support_host": "https://www.tradingview.com"
}
  </script>
</div>'''

      self.solCode = '''<div class="tradingview-widget-container" style="height:100%;width:100%">
  <div class="tradingview-widget-container__widget" style="height:calc(100% - 32px);width:100%"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
  {
  "autosize": true,
  "symbol": "COINBASE:SOLUSD",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "hide_side_toolbar": false,
  "allow_symbol_change": true,
  "support_host": "https://www.tradingview.com"
}
  </script>
</div>'''

      self.chart.setHtml(self.btcCode)
      self.tickerTape.setHtml(tickerTape)

  def mainLayout(self):
    self.gridLayout = QGridLayout()
    self.gridLayout.addWidget(self.tickerTape, 0, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignTop)
    self.gridLayout.addWidget(self.chart, 1, 3, 1, 3, alignment=Qt.AlignmentFlag.AlignRight)

    self.leftLayout = QVBoxLayout()
    self.leftLayout.addWidget(self.combobox)
    
    self.balanceMainLayout = QHBoxLayout()
    self.balanceMainLayout.addWidget(self.balance)

    self.priceLayout = QHBoxLayout()
    self.priceLayout.addWidget(self.price)
    self.priceLayout.addWidget(self.buyBoxAmount)

    self.buyBoxLayout = QHBoxLayout()
    self.buyBoxLayout.addWidget(self.buyBox)
    
    self.sellBoxLayout = QHBoxLayout()
    self.sellBoxLayout.addWidget(self.sellBox)

    self.investedLayout = QHBoxLayout()
    self.investedLayout.addWidget(self.invested)
    self.investedLayout.addWidget(self.sellBoxAmount)

    self.errorLayout = QHBoxLayout()
    self.errorLayout.addWidget(self.error)

    self.buttonsLayout = QHBoxLayout()
    self.buttonsLayout.addWidget(self.buyButton)
    self.buttonsLayout.addWidget(self.sellButton)

    self.buyLayout = QHBoxLayout()
    self.buyLayout.addWidget(self.firstBuyButton)
    self.buyLayout.addWidget(self.secondBuyButton)
    self.buyLayout.addWidget(self.thirdBuyButton)
    self.buyLayout.addWidget(self.fourthBuyButton)

    self.sellLayout = QHBoxLayout()
    self.sellLayout.addWidget(self.firstSellButton)
    self.sellLayout.addWidget(self.secondSellButton)
    self.sellLayout.addWidget(self.thirdSellButton)
    self.sellLayout.addWidget(self.fourthSellButton)

    self.infoLayout = QHBoxLayout()
    self.infoLayout.addWidget(self.investedBtn)
    self.infoLayout.addWidget(self.soldBtn)
    self.infoLayout.addWidget(self.remainBtn)

    self.errorTextLayout = QVBoxLayout()
    self.errorTextLayout.addWidget(self.errorText)
    self.errorWidget.setLayout(self.errorTextLayout)

    self.leftLayout.addLayout(self.balanceMainLayout)
    self.leftLayout.addLayout(self.priceLayout)
    self.leftLayout.addLayout(self.buyBoxLayout)
    self.leftLayout.addLayout(self.buyLayout)
    self.leftLayout.addLayout(self.investedLayout)
    self.leftLayout.addLayout(self.sellBoxLayout)
    self.leftLayout.addLayout(self.sellLayout)
    self.leftLayout.addLayout(self.buttonsLayout)
    self.leftLayout.addLayout(self.infoLayout)

    self.gridLayout.addLayout(self.errorLayout, 3, 0 , 1, 1)
    self.gridLayout.addLayout(self.leftLayout, 1, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignTop)
    self.mainWidget.setLayout(self.gridLayout)

    self.balanceLayout = QVBoxLayout()
    self.balanceLayout.addWidget(self.addBalance)
    self.balanceLayout.addWidget(self.insertBalance)
    self.balanceLayout.addWidget(self.balanceButton)
    self.addBalanceWidget.setLayout(self.balanceLayout)

    self.feesLayout = QVBoxLayout()
    self.feesLayout.addWidget(self.insertFeesText)
    self.feesLayout.addWidget(self.fees)
    self.feesLayout.addWidget(self.insertFees)
    self.feesLayout.addWidget(self.slippage)
    self.feesLayout.addWidget(self.insertSlippage)
    self.feesLayout.addWidget(self.feesButton)
    self.feesWidget.setLayout(self.feesLayout)

    self.firstLayer = QHBoxLayout()
    self.firstLayer.addWidget(self.statsBtc)
    self.firstLayer.addWidget(self.statsEth)
    self.firstLayer.addWidget(self.statsSol)

    self.thirdLayer = QHBoxLayout()
    self.thirdLayer.addWidget(self.soldStatsBtc)
    self.thirdLayer.addWidget(self.soldStatsEth)
    self.thirdLayer.addWidget(self.soldStatsSol)

    self.secondLayer = QHBoxLayout()
    self.secondLayer.addWidget(self.remainStatsBtc)
    self.secondLayer.addWidget(self.remainStatsEth)
    self.secondLayer.addWidget(self.remainStatsSol)

    self.fourthLayer = QHBoxLayout()
    self.fourthLayer.addWidget(self.statsCurrBal)
    self.fourthLayer.addWidget(self.statsBalance)
    self.fourthLayer.addWidget(self.statsSpent)
    self.fourthLayer.addWidget(self.statsWin)

    self.leftLay = QVBoxLayout()
    self.leftLay.addLayout(self.firstLayer)
    self.leftLay.addLayout(self.thirdLayer)
    self.leftLay.addLayout(self.secondLayer)
    self.leftLay.addLayout(self.fourthLayer)
    
    self.firstRightLayer = QHBoxLayout()
    self.firstRightLayer.addWidget(self.timeSpent)

    self.secondRightLayer = QHBoxLayout()
    self.secondRightLayer.addWidget(self.statsReset)

    self.rightLay = QVBoxLayout()
    self.rightLay.addLayout(self.firstRightLayer)
    self.rightLay.addLayout(self.secondRightLayer)

    self.mainStatsLay = QGridLayout()
    self.mainStatsLay.addLayout(self.leftLay, 0,0,2,2)
    self.mainStatsLay.addLayout(self.rightLay, 0,2,2,2, alignment=Qt.AlignmentFlag.AlignTop)
    self.statsWid.setLayout(self.mainStatsLay)


class LoginScreen(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Login")
    self.setMinimumSize(400, 300)
    self.setMaximumSize(500, 400)

    self.loginWidgets()
    self.loginLayout()

  def loginWidgets(self):
    self.usernameInput = QLineEdit()
    self.usernameInput.setPlaceholderText("Name")
    self.passwordInput = QLineEdit()
    self.passwordInput.setPlaceholderText("Password")

    self.loginButton = QPushButton("Login")
    self.registerButton = QPushButton("Register")

    self.registerText = QLabel("Don't have an account? Register here!")

  def loginLayout(self):
    layout = QVBoxLayout()
    layout.addWidget(self.usernameInput, alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.passwordInput, alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.loginButton, alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.registerText, alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.registerButton, alignment=Qt.AlignmentFlag.AlignCenter)
    self.setLayout(layout)

class RegisterScreen(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Register")
    self.setMinimumSize(400, 300)
    self.setMaximumSize(500, 400)

    self.registerWidgets()
    self.registerLayout()

  def registerWidgets(self):
    self.usernameInput = QLineEdit()
    self.usernameInput.setPlaceholderText("Name")
    self.passwordInput = QLineEdit()
    self.passwordInput.setPlaceholderText("Password")
    self.reenterPassword = QLineEdit()
    self.reenterPassword.setPlaceholderText("Re-enter password")

    self.registerBtn = QPushButton("Register")
    self.backButton = QPushButton("Back")

  def registerLayout(self):
    layout = QVBoxLayout()
    layout.addWidget(self.usernameInput, alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.passwordInput, alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.reenterPassword, alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.registerBtn, alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.backButton, alignment=Qt.AlignmentFlag.AlignCenter)
    self.setLayout(layout)