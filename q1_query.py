from db_connect_for_queries import  *

# Q1.)

q_1 = cursor.execute(" SELECT * FROM ORDERS").fetchall()
print(len(q_1))

q_2 = cursor.execute("SELECT * FROM ORDERS WHERE ShipCity = 'Rio de Janeiro'").fetchall()
print(len(q_2))

q_3 = cursor.execute("SELECT * FROM ORDERS WHERE ShipCity = 'Rio de Janeiro' OR ShipCity = 'Reims'").fetchall()
print(len(q_3))

q_4 = cursor.execute("SELECT * FROM Customers WHERE CompanyName LIKE '%z%' ").fetchone()

while True:
    record = q_4.fetchone()
    if record is None:
        break
    print(record)