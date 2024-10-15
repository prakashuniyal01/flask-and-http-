from backend.models.menu_items_model import (
    add_menu_item,
    get_menu_items,
    get_menu_item_by_id,
    update_menu_item,
    delete_menu_item,
    recover_menu_item
)

def handle_menu_request(request, data=None):
    try:
        if 'method' not in request:
            return {"status": "error", "message": "Request method not provided."}
        
        method = request['method'].upper()
        
        if method == 'POST':
            name = data.get('name')
            price = data.get('price')
            category = data.get('category')
            description = data.get('description')  # Get description from the request data

            if not name or not price or not category or not description:
                return {"status": "error", "message": "Missing required fields (name, price, category, description)."}
            if price <= 0:
                return {"status": "error", "message": "Price must be greater than zero."}
            if category not in ['Veg', 'Non-Veg', 'Vegan']:
                return {"status": "error", "message": "Invalid category. Must be 'Veg', 'Non-Veg', or 'Vegan'."}

            return add_menu_item(name, price, category, description)  # Pass description to the model
        
        elif method == 'GET':
            item_id = data.get('item_id') if data else None
            if item_id:
                menu_item = get_menu_item_by_id(item_id)
                if menu_item:
                    return {"status": "success", "data": menu_item}
                else:
                    return {"status": "error", "message": f"Menu item with ID {item_id} not found."}
            else:
                menu_items = get_menu_items()
                return {"status": "success", "data": menu_items}

        elif method == 'PUT':
            item_id = data.get('item_id')
            name = data.get('name')
            price = data.get('price')
            category = data.get('category')
            description = data.get('description')  # Get description from the request data

            if not item_id or not name or not price or not category or not description:
                return {"status": "error", "message": "Missing parameters (item_id, name, price, category, description)."}

            if price <= 0:
                return {"status": "error", "message": "Price must be greater than zero."}
            if category not in ['Veg', 'Non-Veg', 'Vegan']:
                return {"status": "error", "message": "Invalid category. Must be 'Veg', 'Non-Veg', or 'Vegan'."}

            return update_menu_item(item_id, name, price, category, description)  # Pass description to the model
        
        elif method == 'DELETE':
            item_id = data.get('item_id')
            if not item_id:
                return {"status": "error", "message": "Missing menu item ID."}
            return delete_menu_item(item_id)

        elif method == 'RECOVER':
            item_id = data.get('item_id')
            if not item_id:
                return {"status": "error", "message": "Missing menu item ID."}
            return recover_menu_item(item_id)
        
        else:
            return {"status": "error", "message": "Invalid request method."}
    
    except Exception as e:
        return {"status": "error", "message": f"An error occurred: {e}"}
