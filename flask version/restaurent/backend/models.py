# Table model definitions (not an ORM, but helper functions to run queries)
from database import get_db_connection

def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Create Menu Items Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu_items (
            item_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255),
            price DECIMAL(10, 2)
        );
    """)

    # Create Customers Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255),
            phone_number VARCHAR(20)
        );
    """)

    # Create Orders Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INT PRIMARY KEY AUTO_INCREMENT,
            customer_id INT,
            item_id INT,
            quantity INT,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY (item_id) REFERENCES menu_items(item_id)
        );
    """)

    connection.commit()
    cursor.close()
    connection.close()

# Call create_tables when the server starts to ensure the tables exist
create_tables()
