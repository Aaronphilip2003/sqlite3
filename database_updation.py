import sqlite3

conn=sqlite3.connect('customers.db')

cursor=conn.cursor()

cursor.execute("""UPDATE customers SET first_name='AARON' WHERE rowid=1""")

# cursor.execute("INSERT INTO customers VALUES ('aaron','philip','lol2003@gmail.com')")

cursor.execute("DELETE FROM customers WHERE rowid=6")

conn.commit()
conn.close()