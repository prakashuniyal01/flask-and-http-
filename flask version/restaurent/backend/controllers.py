from database import get_db_connection

# Fetch all menu items
def get_all_menu_items():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM menu_items")
    menu_items = cursor.fetchall()
    cursor.close()
    connection.close()
    return menu_items

# Fetch all customers
def get_all_customers():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    cursor.close()
    connection.close()
    return customers

# Fetch order history for a customer
def get_order_history(customer_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM orders WHERE customer_id = %s", (customer_id,))
    orders = cursor.fetchall()
    cursor.close()
    connection.close()
    return orders

# Add new menu item
def add_menu_item(name, price):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO menu_items (name, price) VALUES (%s, %s)", (name, price))
    connection.commit()
    cursor.close()
    connection.close()

# Add new customer
def add_customer(name, phone_number):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO customers (name, phone_number) VALUES (%s, %s)", (name, phone_number))
    connection.commit()
    cursor.close()
    connection.close()

# Place new order
def place_order(customer_id, item_id, quantity):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO orders (customer_id, item_id, quantity, order_date) VALUES (%s, %s, %s, NOW())",
                   (customer_id, item_id, quantity))
    connection.commit()
    cursor.close()
    connection.close()
