# backend/models/order.py
from database.db_connection import get_db_connection
import logging

def place_order(customer_id, item_id, quantity, order_date):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        sql = """
            INSERT INTO orders (customer_id, item_id, quantity, order_date)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (customer_id, item_id, quantity, order_date))
        connection.commit()
        return cursor.lastrowid  # Return the ID of the new order
    except Exception as e:
        logging.error(f"Error placing order: {e}")
        return None
    finally:
        cursor.close()
        connection.close()

def get_order_history(customer_id=None):
    connection = get_db_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        if customer_id:
            sql = """
                SELECT o.order_id, o.customer_id, o.item_id, o.quantity, o.order_date, c.name AS customer_name, m.name AS item_name
                FROM orders o
                JOIN customers c ON o.customer_id = c.customer_id
                JOIN menu_items m ON o.item_id = m.item_id
                WHERE o.customer_id = %s
            """
            cursor.execute(sql, (customer_id,))
        else:
            sql = """
                SELECT o.order_id, o.customer_id, o.item_id, o.quantity, o.order_date, c.name AS customer_name, m.name AS item_name
                FROM orders o
                JOIN customers c ON o.customer_id = c.customer_id
                JOIN menu_items m ON o.item_id = m.item_id
            """
            cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        logging.error(f"Error fetching order history: {e}")
        return []
    finally:
        cursor.close()
        connection.close()

def calculate_total_revenue(start_date, end_date):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        sql = """
            SELECT SUM(o.quantity * m.price) as total_revenue
            FROM orders o
            JOIN menu_items m ON o.item_id = m.item_id
            WHERE o.order_date BETWEEN %s AND %s
        """
        cursor.execute(sql, (start_date, end_date))
        return cursor.fetchone()[0]
    finally:
        cursor.close()
        connection.close()
