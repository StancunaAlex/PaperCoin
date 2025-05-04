from PyQt6.QtCore import Qt
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import (QWidget, QComboBox,
                              QPushButton, QLabel,
                              QLineEdit, QGridLayout,
                              QVBoxLayout, QHBoxLayout,
                              QDoubleSpinBox
)

# Initialize widgets
class Widgets(QWidget):
  def __init__(self):
      super().__init__()

      self.mainWidgets()
      self.mainLayout()

# Add widgets
  def mainWidgets(self):
      
      self.mainWidget = QWidget()
      self.mainWidget.setStyleSheet("background-color: #000000;")

      self.errorWidget = QWidget()
      self.errorWidget.setWindowTitle("Error")

      self.addBalanceWidget = QWidget()
      self.addBalanceWidget.setWindowTitle("Add Balance")
      self.addBalanceWidget.setMaximumSize(200, 96)

      self.feesWidget = QWidget()
      self.feesWidget.setWindowTitle("Configure fees and slippage")
      self.feesWidget.setMaximumSize(200, 116)

      self.chart = QWebEngineView()

      self.tickerTape = QWebEngineView()
      self.tickerTape.setFixedHeight(60)

      self.buyButtonsStyle = """
            QPushButton {
                background-color: #303336;    
                color: #BAC7CF;               
                border-radius: 5px;
                padding: 6px 12px;
            }"""

      textStyle = "color: #BAC7CF;"

      self.activeBuyStyle = """
    QPushButton {
        background-color: #303336;    
        color: #BAC7CF;               
        border: 1px solid #0ABF34;     
        border-radius: 5px;
        padding: 6px 12px;
    }
"""
      self.buyButton = QPushButton("Buy")
      self.buyButton.setStyleSheet("background-color: #0ABF34;")
      self.firstBuyButton = QPushButton("25%")
      self.firstBuyButton.setStyleSheet(self.buyButtonsStyle)
      self.secondBuyButton = QPushButton("50%")
      self.secondBuyButton.setStyleSheet(self.buyButtonsStyle)
      self.thirdBuyButton = QPushButton("75%")
      self.thirdBuyButton.setStyleSheet(self.buyButtonsStyle)
      self.fourthBuyButton = QPushButton("100%")
      self.fourthBuyButton.setStyleSheet(self.buyButtonsStyle)

      self.sellButton = QPushButton("Sell")
      self.sellButton.setStyleSheet("background-color: #BF0A19")
      self.firstSellButton = QPushButton("25%")
      self.firstSellButton.setStyleSheet(self.buyButtonsStyle)
      self.secondSellButton = QPushButton("50%")
      self.secondSellButton.setStyleSheet(self.buyButtonsStyle)
      self.thirdSellButton = QPushButton("75%")
      self.thirdSellButton.setStyleSheet(self.buyButtonsStyle)
      self.fourthSellButton = QPushButton("100%")
      self.fourthSellButton.setStyleSheet(self.buyButtonsStyle)

      self.balanceButton = QPushButton("Accept")
      self.feesButton = QPushButton("Accept")

      self.combobox = QComboBox()
      self.combobox.addItem('Bitcoin')
      self.combobox.addItem('Ethereum')
      self.combobox.addItem('Solana')
      self.combobox.setStyleSheet("""background-color: #303336;
                                  color: #BAC7CF;""")

      self.balance = QLabel("Balance: 0 $")
      self.balance.setStyleSheet(textStyle)
      self.price = QLabel("Price:")
      self.price.setStyleSheet(textStyle)
      self.buyBoxAmount = QLabel("Amount: 0 $")
      self.buyBoxAmount.setStyleSheet(textStyle)
      self.error = QLabel()
      self.error.setStyleSheet(textStyle)
      self.errorText = QLabel()
      self.invested = QLabel("Invested: 0")
      self.invested.setStyleSheet(textStyle)
      self.sellBoxAmount = QLabel("Amount: 0")
      self.sellBoxAmount.setStyleSheet(textStyle)

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
      self.buyBox.setStyleSheet(textStyle)

      self.sellBox = QDoubleSpinBox()
      self.sellBox.setDecimals(15)
      self.sellBox.clear()
      self.sellBox.setStyleSheet(textStyle)

# Store the code from TradingView
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

# Set the code from TradingView
      self.chart.setHtml(self.btcCode)
      self.tickerTape.setHtml(tickerTape)

  def mainLayout(self):
# Main grid layout for the app
    self.gridLayout = QGridLayout()
    self.gridLayout.addWidget(self.tickerTape, 0, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignTop)
    self.gridLayout.addWidget(self.chart, 1, 3, 1, 3, alignment=Qt.AlignmentFlag.AlignRight)

# Add widgets to layouts
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

    self.errorTextLayout = QVBoxLayout()
    self.errorTextLayout.addWidget(self.errorText)
    self.errorWidget.setLayout(self.errorTextLayout)

# Main layout for the left panel
    self.leftLayout.addLayout(self.balanceMainLayout)
    self.leftLayout.addLayout(self.priceLayout)
    self.leftLayout.addLayout(self.buyBoxLayout)
    self.leftLayout.addLayout(self.buyLayout)
    self.leftLayout.addLayout(self.investedLayout)
    self.leftLayout.addLayout(self.sellBoxLayout)
    self.leftLayout.addLayout(self.sellLayout)
    self.leftLayout.addLayout(self.buttonsLayout)

    self.gridLayout.addLayout(self.errorLayout, 3, 0 , 1, 1)
    self.gridLayout.addLayout(self.leftLayout, 1, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignTop)
    
    self.mainWidget.setLayout(self.gridLayout)

# Layout for adding balance
    self.balanceLayout = QVBoxLayout()
    self.balanceLayout.addWidget(self.addBalance)
    self.balanceLayout.addWidget(self.insertBalance)
    self.balanceLayout.addWidget(self.balanceButton)
    
    self.addBalanceWidget.setLayout(self.balanceLayout)

# Layout for adjusting fees and slippage
    self.feesLayout = QVBoxLayout()
    self.feesLayout.addWidget(self.insertFeesText)
    self.feesLayout.addWidget(self.fees)
    self.feesLayout.addWidget(self.insertFees)
    self.feesLayout.addWidget(self.slippage)
    self.feesLayout.addWidget(self.insertSlippage)
    self.feesLayout.addWidget(self.feesButton)

    self.feesWidget.setLayout(self.feesLayout)

# Login window
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

# Login window layout
  def loginLayout(self):
    layout = QVBoxLayout()
    layout.addWidget(self.usernameInput, alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.passwordInput, alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.loginButton, alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.registerText, alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.registerButton, alignment=Qt.AlignmentFlag.AlignCenter)

    self.setLayout(layout)

# Register window
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
    self.emailInput = QLineEdit()
    self.emailInput.setPlaceholderText("Email")
    self.passwordInput = QLineEdit()
    self.passwordInput.setPlaceholderText("Password")
    self.reenterPassword = QLineEdit()
    self.reenterPassword.setPlaceholderText("Re-enter password")

    self.backButton = QPushButton("Back")

# Register window layout
  def registerLayout(self):
    layout = QVBoxLayout()
    layout.addWidget(self.usernameInput, alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.emailInput, alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.passwordInput, alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.reenterPassword, alignment=Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(self.backButton, alignment=Qt.AlignmentFlag.AlignCenter)

    self.setLayout(layout)