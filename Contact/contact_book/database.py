from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# Database connection
def createdatabase(databasename):

    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databasename)

    if not connection.open():
        QMessageBox.warning(
            None,
            "RP Contact",
            f"Database Error : {connection.lastError().text()}",
        )
        return False
    
    createContactTable()
    return True

# Create a contact table
def createContactTable():
    createTableQuery = QSqlQuery()

    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        phone VARCHAR(13) NOT NULL,
        email VARCHAR(50) NOT NULL,
        address VARCHAR(100)
        )
        """
    )
