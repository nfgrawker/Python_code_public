
import pyodbc as db

connection_string = "Trusted_Connection=yes; DRIVER={SQL Server}; SERVER=LAPTOP-5QTN78N9\SQLEXPRESS; DATABASE=JoshyJosh"

con = db.connect(connection_string)
cur = con.cursor()

query = "select * from client"

cur.execute(query)
rslt = cur.fetchall()

result = []
for i in rslt:
    result.append(list(i))

query = "insert into client select ?, ?, ?, ?, ?, ?, ?, ?, ?"

for i in result:
    cur.execute(query, i)

cur.commit()
