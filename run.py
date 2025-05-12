import sys
from database import startDb
from logic import Login
from PyQt6.QtWidgets import QApplication

def main():
    startDb()

    app = QApplication(sys.argv)
    start = Login()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()