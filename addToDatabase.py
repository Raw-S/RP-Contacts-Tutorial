from rpcontacts.database import createConnection

 # Create a connection
createConnection("contacts.sqlite")

# Confirm that contacts table exists
from PyQt5.QtSql import QSqlDatabase
db = QSqlDatabase.database()
print("TABLES: " + str(db.tables()))


# Prepare a query to insert sample data
from PyQt5.QtSql import QSqlQuery

insertDataQuery = QSqlQuery()
insertDataQuery.prepare(
     """
     INSERT INTO contacts (
         name,
        job,
        email
     )
     VALUES (?, ?, ?)
     """
 )

data = [
     ("Linda", "Technical Lead", "linda@example.com"),
     ("Joe", "Senior Web Developer", "joe@example.com"),
     ("Lara", "Project Manager", "lara@example.com"),
     ("David", "Data Analyst", "david@example.com"),
     ("Jane", "Senior Python Developer", "jane@example.com"),
 ]

# Insert sample data
for name, job, email in data:
 insertDataQuery.addBindValue(name)
 insertDataQuery.addBindValue(job)
 insertDataQuery.addBindValue(email)
 insertDataQuery.exec()


