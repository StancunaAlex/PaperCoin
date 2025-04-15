import sys
from main import InitLogin
from PyQt6.QtWidgets import QApplication

def main():
    paperCoin = QApplication(sys.argv)

    start = InitLogin()
    
    paperCoin.exec()

if __name__ == "__main__":
    main()