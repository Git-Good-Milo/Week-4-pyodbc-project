from oop_db_connect import *

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

db_nw = ConnectMsS(server, database, username, password)
print(db_nw)
print(db_nw.conn_nwdb)

print(db_nw.cursor.execute("SELECT * FROM Products").fetchone())

#print(db_nw.__sql_query("SELECT * FROM Products").fetchone()) nTHis is broken for some reason

db_nw.avg_unit_price_prod()