# models/menu_item.py

from database.db_connection import get_db_connection

def add_menu_item(name, price):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO menu_items (name, price) VALUES (%s, %s)"  # Use %s for SQL parameter
        cursor.execute(sql, (name, price))
        connection.commit()
    except Exception as e:
        print(f"Error adding menu item: {e}")  # Handle any potential errors
    finally:
        cursor.close()
        connection.close()

def get_menu_items():
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM menu_items"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching menu items: {e}")  # Handle any potential errors
    finally:
        cursor.close()
        connection.close()
