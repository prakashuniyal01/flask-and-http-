from backend.database.db_connection import get_db_connection

def create_menu_items_table():
    """
    Function to create the 'menu_items' table if it doesn't exist.
    """
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        # SQL statement to create the table if it doesn't exist
        sql = """
        CREATE TABLE IF NOT EXISTS menu_items (
            item_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,  
            price DECIMAL(10, 2) NOT NULL,
            category ENUM('Veg', 'Non-Veg', 'Vegan') NOT NULL,
            status ENUM('active', 'deleted') DEFAULT 'active' NOT NULL,
            description VARCHAR(255) NOT NULL
        );
        """
        cursor.execute(sql)
        connection.commit()
        print("Menu items table created or already exists.")
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        cursor.close()
        connection.close()

def add_menu_item(name, price, category, description):
    """
    Function to add a new menu item. Checks description length and for duplicate items.
    """
    create_menu_items_table()  # Ensure table exists before inserting item
    connection = get_db_connection()
    try:
        cursor = connection.cursor()

        # Validate description length (should not exceed 100 words)
        if len(description.split()) > 100:
            return {"status": "error", "message": "Description cannot exceed 100 words."}

        # Check if category is valid
        valid_categories = ['Veg', 'Non-Veg', 'Vegan']
        if category not in valid_categories:
            return {"status": "error", "message": "Invalid category. Must be 'Veg', 'Non-Veg', or 'Vegan'."}

        # Check if the item already exists with the same name and category
        sql_check = "SELECT * FROM menu_items WHERE name = %s AND category = %s"
        cursor.execute(sql_check, (name, category))
        existing_item = cursor.fetchone()

        if existing_item:
            if existing_item[4] == 'active':  # Check if the item is active
                return {"status": "error", "message": f"Menu item '{name}' in '{category}' category already exists and is active."}
            elif existing_item[4] == 'deleted':  # If the item is soft deleted
                return {
                    "status": "error", 
                    "message": f"Menu item '{name}' in '{category}' category exists but is deleted. Please recover it instead."
                }

        # Insert new item if not a duplicate
        sql_insert = "INSERT INTO menu_items (name, price, category, description) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql_insert, (name, price, category, description))
        connection.commit()

        return {"status": "success", "message": f"Menu item '{name}' added successfully."}

    except Exception as e:
        return {"status": "error", "message": f"An error occurred: {e}"}
    
    finally:
        cursor.close()
        connection.close()

def get_menu_items():
    """
    Function to fetch all active menu items.
    """
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM menu_items WHERE status = 'active'"
        cursor.execute(sql)
        items = cursor.fetchall()

        # Format items
        formatted_items = [
            {
                "item_id": item[0],
                "name": item[1],
                "price": float(item[2]),  # Convert Decimal to float
                "category": item[3],
                "status": item[4],
                "description": item[5]
            }
            for item in items
        ]
        return formatted_items
    except Exception as e:
        print(f"Error fetching menu items: {e}")
    finally:
        cursor.close()
        connection.close()

def get_menu_item_by_id(item_id):
    """
    Function to fetch a specific menu item by its ID.
    """
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM menu_items WHERE item_id = %s"
        cursor.execute(sql, (item_id,))
        item = cursor.fetchone()

        if item:
            return {
                "item_id": item[0],
                "name": item[1],
                "price": float(item[2]),
                "category": item[3],
                "status": item[4],
                "description": item[5]
            }
        else:
            return None  # Return None if item not found
    except Exception as e:
        print(f"Error fetching menu item: {e}")
    finally:
        cursor.close()
        connection.close()

def update_menu_item(item_id, name, price, category, description):
    """
    Function to update an existing menu item.
    """
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        existing_item = get_menu_item_by_id(item_id)
        if not existing_item:
            return {"status": "error", "message": f"Menu item with ID {item_id} not found."}

        # Validate description length (should not exceed 100 words)
        if len(description.split()) > 100:
            return {"status": "error", "message": "Description cannot exceed 100 words."}

        sql = "UPDATE menu_items SET name = %s, price = %s, category = %s, description = %s WHERE item_id = %s"
        cursor.execute(sql, (name, price, category, description, item_id))
        connection.commit()
        return {"status": "success", "message": f"Menu item with ID {item_id} updated successfully."}
    except Exception as e:
        return {"status": "error", "message": f"Error updating menu item: {e}"}
    finally:
        cursor.close()
        connection.close()

def delete_menu_item(item_id):
    """
    Function to soft delete a menu item by marking its status as 'deleted'.
    """
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        existing_item = get_menu_item_by_id(item_id)
        if not existing_item:
            return {"status": "error", "message": f"Menu item with ID {item_id} not found."}

        # Soft delete: Mark status as 'deleted'
        sql = "UPDATE menu_items SET status = 'deleted' WHERE item_id = %s"
        cursor.execute(sql, (item_id,))
        connection.commit()
        return {"status": "success", "message": f"Menu item with ID {item_id} deleted successfully."}
    except Exception as e:
        return {"status": "error", "message": f"Error deleting menu item: {e}"}
    finally:
        cursor.close()
        connection.close()

def recover_menu_item(item_id):
    """
    Function to recover a soft-deleted menu item by marking its status back to 'active'.
    """
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        existing_item = get_menu_item_by_id(item_id)
        if not existing_item:
            return {"status": "error", "message": f"Menu item with ID {item_id} not found."}

        if existing_item["status"] == "active":
            return {"status": "error", "message": f"Menu item with ID {item_id} is already active."}

        # Recover: Mark status as 'active'
        sql = "UPDATE menu_items SET status = 'active' WHERE item_id = %s"
        cursor.execute(sql, (item_id,))
        connection.commit()
        return {"status": "success", "message": f"Menu item with ID {item_id} recovered successfully."}
    except Exception as e:
        return {"status": "error", "message": f"Error recovering menu item: {e}"}
    finally:
        cursor.close()
        connection.close()
