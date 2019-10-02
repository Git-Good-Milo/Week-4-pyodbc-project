import pyodbc
# In this file well make our connection

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Estabilsh connection
conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
#print(conn_nwdb)




# Create a curser
# Allows us to execute read only queries

cursor = conn_nwdb.cursor()

cursor.execute("SELECT * FROM CUSTOMERS;")

# using.execute() on a cursor
#print(cursor)


# print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

# Fetch all .fetchall()
# This is bad MMk'kay
# We dont use this MM'kay...
#rows = cursor.execute("SELECT * FROM CUSTOMERS").fetchall()

#)print(rows)
#print(len(rows))

# rows = cursor.execute("SELECT * FROM PRODUCTS").fetchall()

# for record in rows:
#     print(type(record))
#     print(record.UnitPrice) # We can access the colomn of a specific record

# However, this is dangerous. we can clog our machine with too much data
# We can use while loops to be more effcient

rows  = cursor.execute("SELECT * FROM PRODUCTS")

while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice)

# Fetch

