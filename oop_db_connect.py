import pyodbc

# Concept of 'Strong Params'
    # Never EVER TRUST user input
    # Avoid SQL Injections
    # Filter from SQL injections

class ConnectMsS():

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn_nwdb.cursor()

    def __filter_query(self, query):
        # Doing some filtering for bad queries
        return self.cursor.execute(query)

    def __sql_query(self, query):
        return self.filter_query(query)

    def __sql_query_fetchone(self, query):
        return self.__filter_query(query).fetchone()

    def print_all_product_records(self):
        query_rows = self.__filter_query("SELECT * FROM Products")
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            print(record)

    def avg_unit_price_prod(self):
        query_rows = self.__filter_query("SELECT AVG(UnitPrice) FROM Products").fetchone()
        return print(query_rows)




    # CRUD

    # Create 1 entry
        # Use INSERT
        # The cursor cannot make transactions (Go to documentation)



    # Read all enteries
        # Fetch all records as a List of Diciontaies
    def read_all_sql_entries(self, table):
        query_entry = self.__filter_query(f"SELECT * FROM {table}")
        while True:
            record = query_entry.fetchone()
            if record is None:
                break
            print(record)

    # Read one entry
        # Fetch a specific Record
        # Get one value using ID
    def read_one_sql_id(self, table, id, number):
        query_entry = self.__filter_query(f"SELECT * FROM {table} WHERE {id} = {number} ").fetchone()
        return query_entry

    # Update 1 Entry
        # The ID of the record to update
        # Update the specific record
            # The cursor cannot make transactions (go to documentaion)

    # Destroy ine entry
        # THe ID of the specific record
        # Destroy the record
            # The Cursor cannot make transaction (got to dicumentaion)



