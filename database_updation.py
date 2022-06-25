import sqlite3

conn=sqlite3.connect('customers.db')

cursor=conn.cursor()

cursor.execute("""UPDATE customers SET first_name='AARON' WHERE rowid=1""")

conn.commit()
conn.close()