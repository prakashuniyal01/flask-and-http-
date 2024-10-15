
### create customers table 
    CREATE TABLE customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT, -- Auto-incremented ID
        name TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE, -- Username must be unique
        phone_number TEXT NOT NULL UNIQUE, -- Phone number must be unique
        CHECK (LENGTH(phone_number) >= 10) -- Ensure phone number has at least 10 digits
    );


### menu items 
    CREATE TABLE IF NOT EXISTS menu_items (
        item_id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100) NOT NULL,  
        price DECIMAL(10, 2) NOT NULL,
        category ENUM('Veg', 'Non-Veg', 'Vegan') NOT NULL,
        status ENUM('active', 'deleted') DEFAULT 'active' NOT NULL
    );


-- Ensures the menu name is unique

 -- Limits category to specific values
    