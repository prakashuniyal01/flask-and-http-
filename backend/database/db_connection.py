import mysql.connector

# Database connection setup for MySQL
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',         
        password='root',     
        database='restaurant_manage'
    )
    return connection
