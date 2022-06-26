import sqlite3

conn = sqlite3.connect("customers.db")

cursor=conn.cursor()

cursor.execute("SELECT rowid, * FROM customers")
# cursor.execute("SELECT rowid, * FROM customers")

# cursor.execute("SELECT * FROM customers WHERE first_name='AARON'")

# cursor.fetchone()
# cursor.fetchmany(3)

# cursor.execute("INSERT INTO customers VALUES ('NEERAJ','VARMA','neerajvarma2003@gmail.com')")

items=cursor.fetchall()

for item in items:
    print(item)



conn.commit()
conn.close()