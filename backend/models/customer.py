# models/customer.py
from database.db_connection import get_db_connection

def add_customer(name, phone_number):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO customers (name, phone_number) VALUES (%s, %s)"  # Use %s for PostgreSQL
        cursor.execute(sql, (name, phone_number))
        connection.commit()
    except Exception as e:
        print(f"Error adding customer: {e}")
    finally:
        cursor.close()
        connection.close()

def get_customers():
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM customers"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching customers: {e}")
    finally:
        cursor.close()
        connection.close()
