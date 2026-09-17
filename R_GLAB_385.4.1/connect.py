# to connect to mysql database 
# we need to install mysql-connector-python package
import mysql.connector as mydbconnection  # type: ignore[reportMissingImports]
from mysql.connector import Error  # type: ignore[reportMissingImports]
def connect():
 connection : None
 

try:
        connection = mydbconnection.connect(
            database='classicmodels',
            user='root',
            password='Raqeeb@123'
        )
        if connection.is_connected():
                    print('Connected to MySQL database')
                    print('Connected to MySQL database')
except Error as e:
        print(f'Error while connecting to MySQL: {e}')
finally:
        if connection is not None and connection.is_connected():
                        connection.close()
                        print('MySQL connection is closed')
       
                
if __name__ == '__main__':
  connect()
