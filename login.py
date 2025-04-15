from mainWidgets import LoginScreen
from PyQt6.QtWidgets import QWidget, QVBoxLayout

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setMinimumSize(400, 300)
        self.setMaximumSize(500, 400)
        
        self.loginScreen = LoginScreen()

        layout = QVBoxLayout()
        layout.addWidget(self.loginScreen)

        self.setLayout(layout)