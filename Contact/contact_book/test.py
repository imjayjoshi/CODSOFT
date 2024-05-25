import os
from database import createConnection
from PyQt5.QtSql import QSqlDatabase

file = os.path.join(os.path.realpath(__file__), "contacts.sqlite3")
createConnection(file)

# confirm contact table exist or not
db = QSqlDatabase.database()
print(db.tables())
db.tables()