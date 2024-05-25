from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from .model import Contacts

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Contact Book")
        self.setFixedSize(600, 400)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.contacts = Contacts()
        self.setupUI()

    def setupUI(self):
        self.table = QTableView()
        self.table.setModel(self.contacts.model)
        self.table.resizeColumnsToContents()

        self.searchfield = QLineEdit()
        self.searchfield.setPlaceholderText("Search...")
        self.searchfield.textChanged.connect(self.searchContact)

        self.addbtn = QPushButton("Add Contact")
        self.addbtn.clicked.connect(self.openAddDialog)
        self.updatebtn = QPushButton("Update Contact")
        self.updatebtn.clicked.connect(self.openUpdateDialog)
        self.dltbtn = QPushButton("Delete Contact")
        self.dltbtn.clicked.connect(self.DltContact)
        self.clrallbtn = QPushButton("Clear All")
        self.clrallbtn.clicked.connect(self.ClrContact)

        layout = QVBoxLayout()
        layout.addWidget(self.searchfield)
        layout.addWidget(self.addbtn)
        layout.addWidget(self.updatebtn)
        layout.addWidget(self.dltbtn)
        layout.addStretch()
        layout.addWidget(self.clrallbtn)

        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def openAddDialog(self):
        dialog = ContactDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.contacts.addcontact(dialog.data)
            self.table.resizeColumnsToContents()

    def openUpdateDialog(self):
        row = self.table.currentIndex().row()
        if row < 0:
            return

        dialog = ContactDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.contacts.updatecontact(row, dialog.data)
            self.table.resizeColumnsToContents()

    def DltContact(self):
        row = self.table.currentIndex().row()
        if row < 0:
            return
        
        message = QMessageBox.warning(
            self, 
            "Warning",
            "Do you want to delete the selected contact?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if message == QMessageBox.Ok:
            self.contacts.removecontact(row)
    
    def ClrContact(self):
        message = QMessageBox.warning(
            self, 
            "Warning",
            "Do you want to remove all contacts?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if message == QMessageBox.Ok:
            self.contacts.clearcontact()

    def searchContact(self, text):
        self.table.setModel(self.contacts.searchcontacts(text))
        self.table.resizeColumnsToContents()

class ContactDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setWindowTitle("Contact")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        self.namefield = QLineEdit()
        self.namefield.setObjectName("Name")
        self.phonefield = QLineEdit()
        self.phonefield.setObjectName("Phone No")
        self.emailfield = QLineEdit()
        self.emailfield.setObjectName("Email")
        self.addressfield = QLineEdit()
        self.addressfield.setObjectName("Address")

        layout = QFormLayout()
        layout.addRow("Name:", self.namefield)
        layout.addRow("Phone No:", self.phonefield)
        layout.addRow("Email:", self.emailfield)
        layout.addRow("Address:", self.addressfield)
        self.layout.addLayout(layout)

        self.btnBox = QDialogButtonBox(self)
        self.btnBox.setOrientation(Qt.Horizontal)
        self.btnBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.btnBox.accepted.connect(self.accept)
        self.btnBox.rejected.connect(self.reject)
        self.layout.addWidget(self.btnBox)

    def accept(self):
        self.data = []
        for field in (self.namefield, self.phonefield, self.emailfield, self.addressfield):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a contact's {field.objectName()}",
                )
                self.data = None
                return
            self.data.append(field.text())

        if not self.data:
            return

        super().accept()
