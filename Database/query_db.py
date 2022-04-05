import sqlite3

# Connect to database
conn = sqlite3.connect("customer.db")

c = conn.cursor()
c.execute("SELECT rowid, * FROM customers WHERE last_name = 'Elder'")

# c.fetchone()
# c.fetchmany()

customers = c.fetchall()
for customer in customers:
    print(customer[0], " ", customer[1])
c.close()
