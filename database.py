import sqlite3

conn = sqlite3.connect("customers.db")

cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS customers(
    first_name text,
    last_name text,
    email text
)"""
)


# cursor.execute(
#     "INSERT INTO customers VALUES ('ALLAN','PHILIP','allanphilip2003@gmail.com')"
# )

# many_customers=[('VIVAN','PODUVAL','vivanpoduval@gmail.com'),
#                 ('ESSA','RABBANI','essafaisal@gmail.com'),
#                 ('SANKALP','PIDIYAR','sankalp.pidiyar@gmail.com'),
# ]

# cursor.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)


conn.commit()

conn.close()
