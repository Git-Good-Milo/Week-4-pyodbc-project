# How to connect SQL to Python using pyodbc :taco:

This is an example of us connecting our sql server, using python and pyodbs

WE will look into:
- Curising
- Rows
- Querying th db 
- USing While Loops for efficient data queries
- Transactions
- (More info at https://github.com/mkleehammer/pyodbc/wiki)

## Connection




## .cursor()
- This method allows us to execute read only queries. The Cursor object represents a database cursor, which is typically used to manage the context of a fetch operation

## .execute()
-  Prepares and executes a SQL statement

## cursor.execute()
- used to execute read only SQL query statments

## .fetchall() vs fetchone()
- Returns a list of all the remaining rows in the query VS Returns the next row in the query, or None when no more data is available.