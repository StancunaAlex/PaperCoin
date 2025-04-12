import sys
from main import MainWindow
from login import LoginWindow
from register import RegisterWindow
from PyQt6.QtWidgets import QApplication

class InitApp:
    def __init__(self):
        self.paperCoin = QApplication(sys.argv)

        self.loginWindow = LoginWindow()
        self.registerWindow = RegisterWindow()

        self.loginWindow.registerButton.clicked.connect(self.showRegisterWindow)
        self.registerWindow.backButton.clicked.connect(self.showLoginWindow)
        self.loginWindow.loginButton.clicked.connect(self.showMainWindow)

    def showMainWindow(self):
        self.window = MainWindow()
        self.window.show()
        self.loginWindow.close()
        
    def showRegisterWindow(self):
        self.loginWindow.hide()
        self.registerWindow.show()

    def showLoginWindow(self):
        self.loginWindow.show()
        self.registerWindow.hide()

    def run(self):
        self.loginWindow.show()
        self.paperCoin.exec()

paperCoin = InitApp()
paperCoin.run()