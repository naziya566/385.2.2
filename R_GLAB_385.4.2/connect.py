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
    # Error handling for connection and query execution
    try:
        conn = mydbconnection.connect(
            database='usersdb',
            user='root',
            password='YES' # password for mysql server
        )

        if conn.is_connected():
            # checking if the connection is established
            print(' Connected to MySQL database.')

        # Creates a cursor object that allows SQL actions to the MySQL server engine
        cursor = conn.cursor()

# Create a SQL Query we want to run
        query = '''
            CREATE TABLE laptop (
                ID int(11) NOT NULL,
                Name varchar(250) NOT NULL,
                Price float NOT NULL,
                Purchase_date date NOT NULL
            )
        '''

        cursor.execute(query)

        print('Created Table')

        query = '''
            INSERT INTO laptop (Id, Name, Price, Purchase_date)
            VALUES (13, 'Mac Air M1', 1000, '2021-08-15')
        '''

        cursor.execute(query)
        print('Query Executed.')

        conn.commit()
        print(' Transaction Committed.')
        print(f' {cursor.rowcount}: Record inserted successfully.')

    except Error as e:
        print(f' Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection Closed')



if __name__ == "__main__":
    connect()