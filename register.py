from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QPushButton, QLineEdit,
    QVBoxLayout
)

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Register")
        self.setMinimumSize(400, 300)

        self.initUI()

    def initUI(self):
        
        self.usernameInput = QLineEdit("Name")
        self.emailInput = QLineEdit("Email")
        self.passwordInput = QLineEdit("Password")
        self.reenterPassword = QLineEdit("Re-enter password")

        self.backButton = QPushButton("Back")

        self.layoutUI()

    def layoutUI(self):
        
        layout = QVBoxLayout()
        layout.addWidget(self.usernameInput, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.emailInput, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.passwordInput, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.reenterPassword, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.backButton, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)