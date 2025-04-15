from PyQt6.QtCore import Qt
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import (QWidget, QComboBox,
                              QPushButton, QLabel,
                              QLineEdit, QGridLayout,
                              QVBoxLayout, QHBoxLayout
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

      self.addBalanceWidget = QWidget()
      self.addBalanceWidget.setWindowTitle("Add Balance")

      self.chart = QWebEngineView()

      self.tickerTape = QWebEngineView()
      self.tickerTape.setFixedHeight(60)

      self.buyButton = QPushButton("Buy")
      self.buyButton.setStyleSheet("background-color: #0CDB3C;")

      self.sellButton = QPushButton("Sell")
      self.sellButton.setStyleSheet("background-color: #DB0B1D")

      self.balanceButton = QPushButton("Accept")

      self.combobox = QComboBox()
      self.combobox.addItem('Bitcoin')
      self.combobox.addItem('Ethereum')
      self.combobox.addItem('Solana')
      self.combobox.setStyleSheet("background-color: #FFFFFF;")

      self.balance = QLabel("Balance:")
      self.balance.setStyleSheet("color: #FFFFFF;")
      self.price = QLabel("Price:")
      self.price.setStyleSheet("color: #FFFFFF;")

      self.addBalance = QLabel("Add the balance amount:")

      self.insertBalance = QLineEdit()

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

# Add widgets for layouts
    self.leftLayout = QVBoxLayout()
    self.leftLayout.addWidget(self.combobox, alignment=Qt.AlignmentFlag.AlignTop)
    
    self.balanceMainLayout = QHBoxLayout()
    self.balanceMainLayout.addWidget(self.balance)

    self.priceLayout = QHBoxLayout()
    self.priceLayout.addWidget(self.price)

    self.buttonsLayout = QHBoxLayout()
    self.buttonsLayout.addWidget(self.buyButton)
    self.buttonsLayout.addWidget(self.sellButton)

# Main layout for the left panel
    self.leftLayout.addLayout(self.balanceMainLayout)
    self.leftLayout.addLayout(self.priceLayout)
    self.leftLayout.addLayout(self.buttonsLayout)
    self.gridLayout.addLayout(self.leftLayout, 1, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignTop)
    
    self.mainWidget.setLayout(self.gridLayout)

# Layout for adding balance
    self.balanceLayout = QVBoxLayout()
    self.balanceLayout.addWidget(self.addBalance)
    self.balanceLayout.addWidget(self.insertBalance)
    self.balanceLayout.addWidget(self.balanceButton)
    
    self.addBalanceWidget.setLayout(self.balanceLayout)

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