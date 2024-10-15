import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",       # Replace with your MySQL username
        password="root",   # Replace with your MySQL password
        database="restaurant_db"    # Replace with your database name
    )
    return connection
