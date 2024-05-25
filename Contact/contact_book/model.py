from PyQt5.QtSql import QSqlTableModel, QSqlQuery
from PyQt5.QtCore import Qt

class Contacts:
    def __init__(self):
        self.model = self._createmodel()

    @staticmethod
    def _createmodel():
        table = QSqlTableModel()
        table.setTable("contacts")
        table.setEditStrategy(QSqlTableModel.OnFieldChange)
        table.select()

        headers = ("ID", "Name", "Phone No", "Email", "Address")
        for columnIndex, header in enumerate(headers):
            table.setHeaderData(columnIndex, Qt.Horizontal, header)
        return table
    
    def addcontact(self, data):
        row = self.model.rowCount()
        self.model.insertRow(row)
        for column_index, field in enumerate(data):
            self.model.setData(self.model.index(row, column_index + 1), field)
        self.model.submitAll()
        self.model.select()

    def updatecontact(self, row, data):
        for column_index, field in enumerate(data):
            self.model.setData(self.model.index(row, column_index + 1), field)
        self.model.submitAll()
        self.model.select()

    def removecontact(self, row):
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def clearcontact(self):
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()

    def searchcontacts(self, text):
        query = QSqlQuery()
        query.prepare("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ? OR email LIKE ? OR address LIKE ?")
        query.addBindValue(f"%{text}%")
        query.addBindValue(f"%{text}%")
        query.addBindValue(f"%{text}%")
        query.addBindValue(f"%{text}%")
        query.exec_()

        model = QSqlTableModel()
        model.setQuery(query)
        return model
