### Restaurant-Order-Management-System/
    │
    ├── backend/
    │   ├── controllers/
    │   │   ├── menu_controller.py      # Handles menu related logic
    │   │   ├── customer_controller.py  # Handles customer related logic
    │   │   └── order_controller.py     # Handles order related logic
    │   │
    │   ├── models/
    │   │   ├── menu_item.py            # Menu item database model
    │   │   ├── customer.py             # Customer database model
    │   │   └── order.py                # Order database model
    │   │
    │   ├── routes/
    │   │   ├── menu_routes.py          # Routes for menu endpoints
    │   │   ├── customer_routes.py      # Routes for customer endpoints
    │   │   └── order_routes.py         # Routes for order endpoints
    │   │
    │   ├── utils/
    │   │   └── helpers.py              # Utility functions (e.g., date formatting, revenue calculation)
    │   │
    │   ├── database/
    │   │   └── db_connection.py        # SQLite database connection setup
    │   │
    │   └── server.py                   # Main server file to run the HTTP server
    │
    └── frontend/
        ├── css/
        │   └── styles.css              # CSS styles for the frontend
        │
        ├── js/
        │   └── app.js                  # JavaScript file to handle frontend logic
        │
        ├── index.html                  # Home page for placing orders, viewing menu
        └── order_history.html          # Page for viewing order history


# Database connection setup for MySQL 
    make sure your local system installed in my sql and change your configes accourding your system 

    def get_db_connection():
        connection = mysql.connector.connect(
            host='localhost',
            user='root',         
            password='root',     
            database='restaurant_manage'
        )
        return connection

    than your connections are cofigered than create you database and insert all tables below instructions 

    CREATE DATABASE restaurant_manage;
    USE restaurant_db;
    CREATE TABLE menu_items (
        item_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2) NOT NULL
    );

    CREATE TABLE customers (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone_number VARCHAR(15) NOT NULL
    );

    CREATE TABLE orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        item_id INT,
        quantity INT,
        order_date DATE,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (item_id) REFERENCES menu_items(item_id)
    );


## run your backend

    -- make sure your db is working 
    -- than change your working dir.. and go the backend dir..
    -- than you can activate your virtual env file 
    -- if your are in linux and mac you use the command =>
    -- source .venv/bin/activate 
    -- pip install mysql-connector-python
    -- python server.py

## run your fruntend 
    its a simple go in index.html page and live your project using your vs code extensions 