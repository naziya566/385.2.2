# To create virtual env - in terminal run: `python3 -m venv .venv`
# Create `.gitignore` file at the ROOT of the project (next to the .venv, NOT IN)
# Document `.venv/` inside `.gitignore`
# Activate env-In terminal: `source .venv/Scripts/activate`
# pip install mysql-connector-python
# Importing MYSQL

import mysql.connector as mydbconnection # using an alias for clarity
from mysql.connector import Error # Error function for special MySQL errors

# Function to connect to MySQL database and insert a record into the laptop table
def connect():
    conn = None
# error handling for connection and query execution
    try:
        conn = mydbconnection.connect(
            database='usersdb',
            user='root',
            password='Raqeeb@123' # password for mysql server
        )

        if conn.is_connected():
            # checking if the connection is established
            print(' Connected to MySQL database.')

        # Creates a cursor object that allows SQL actions to the MySQL server engine
        cursor = conn.cursor()

        # Create a SQL Query we want to run
        query = '''
            INSERT INTO laptop (Id, Name, Price, Purchase_date)
            VALUES (13, 'Mac Air M1', 1000, '2021-08-15')
        '''

        # Executes query in SQL engine/server
        cursor.execute(query)
        print('Query Executed.')
# Commit the transaction to save changes to the database
        conn.commit()
        print('Transaction Commited.')
# Print the number of records inserted successfully
        print(f'{cursor.rowcount}: Record inserted successfully.')
# Close the cursor to free up resources 
    except Error as e:
        print(f'Error: {e}')
# Close the connection to the database in the finally block to ensure it happens regardless of success or failure
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print(' Connection Closed')
