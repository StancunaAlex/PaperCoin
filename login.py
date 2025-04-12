from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QPushButton, QLineEdit,
    QVBoxLayout, QLabel
    )

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setMinimumSize(400, 300)
        self.setMaximumSize(500, 400)
        
        self.initUI()

    def initUI(self):

        self.usernameInput = QLineEdit("Name")
        self.passwordInput = QLineEdit("Password")

        self.loginButton = QPushButton("Login")
        self.registerButton = QPushButton("Register")

        self.registerText = QLabel("Don't have an account? Register here!")

        self.layoutUI()

    def layoutUI(self):

        layout = QVBoxLayout()
        layout.addWidget(self.usernameInput, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.passwordInput, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.loginButton, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.registerText, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.registerButton, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
