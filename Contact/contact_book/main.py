import sys
from PyQt5.QtWidgets import QApplication
from contact_book.views import Window
from contact_book.database import createdatabase

def main():
    app = QApplication(sys.argv)

    if not createdatabase("contacts.sqlite3"):
        sys.exit(1)

    win = Window()
    win.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
