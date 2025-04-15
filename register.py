from mainWidgets import RegisterScreen
from PyQt6.QtWidgets import QWidget, QVBoxLayout

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Register")
        self.setMinimumSize(400, 300)
        self.setMaximumSize(500, 400)

        self.registerScreen = RegisterScreen()

        layout = QVBoxLayout()
        layout.addWidget(self.registerScreen)

        self.setLayout(layout)