import sqlite3

# Create connection
conn  = sqlite3.connect("customer.db")
# Using PC memory
# conn_memory = sqlite3.connect(":memory:")

# Create a cursor
cursor = conn.cursor()

# def create_table(args):
#     # Create a table dot string qoutation mark
#     cursor.execute("CREATE TABLE customers (first_name text,last_name text,email text)")

#     # Commit our command


# # edit_table()
# many_customers = [
#     ('West','Brown', 'west@brown.com'),
#     ('Stephen', 'Mary', 'stephmary@gmail.com'),
#     ('Den', 'James', 'James@den.com')
#     ]

# # Executing multiple data
# cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# # Create single data
# cursor.execute("INSERT INTO customers VALUES ('John','Elder', 'john_elder@gmail.com')")

# Delete 
cursor.execute("DELETE FROM customers WHERE first_name ='John'")

conn.commit()
# Close connection everytime
conn.close()


# 