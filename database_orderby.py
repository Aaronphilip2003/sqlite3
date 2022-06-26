import sqlite3

conn=sqlite3.connect("customers.db")
cursor=conn.cursor()
cursor.execute("SELECT rowid,* FROM customers ORDER BY last_name")
items=cursor.fetchall()
for i in items:
    print(i)
conn.commit()
conn.close()