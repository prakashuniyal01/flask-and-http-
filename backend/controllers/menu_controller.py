from models.menu_item import add_menu_item, get_menu_items

def handle_menu_request(request, data=None):
    if request['method'] == 'POST':
        # Data extraction from the request body
        name = data['name']
        price = data['price']
        
        # Call to add_menu_item function
        add_menu_item(name, price)
        
        # Return success response
        return {
            "status": "success",
            "message": "Menu item added"
        }
    
    elif request['method'] == 'GET':
        # Fetch menu items
        menu_items = get_menu_items()
        
        # Return success response with menu items
        return {
            "status": "success",
            "data": menu_items
        }

    # Handle other methods if needed
    return {
        "status": "error",
        "message": "Invalid request method"
    }
