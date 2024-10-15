from database.db_connection import get_db_connection


# from database.db_connection import get_db_connection

def add_customer(name, username, phone_number):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Insert new customer into the customers table
        sql = "INSERT INTO customers (name, username, phone_number) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, username, phone_number))
        
        conn.commit()
        print("Customer added successfully!")
        # conn.close()
        
    except Exception as e:
        print(f"Error adding customer: {e}")
        
    finally:
        cursor.close()
        conn.close()
        
def get_customers():
    try:
        cunn = get_db_connection()
        cursor = cunn.cursor()
        sql = "SELECT * FROM customers"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching customers: {e}")

    finally:
        cursor.close()
        cunn.close()
        
        