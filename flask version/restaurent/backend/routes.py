from flask import Blueprint, jsonify, request
from controllers import get_all_menu_items, get_all_customers, get_order_history, add_menu_item, add_customer, place_order

api_routes = Blueprint('api_routes', __name__)

# Get all menu items
@api_routes.route('/menu', methods=['GET'])
def fetch_all_menu_items():
    menu_items = get_all_menu_items()
    return jsonify(menu_items), 200

# Get all customers
@api_routes.route('/customers', methods=['GET'])
def fetch_all_customers():
    customers = get_all_customers()
    return jsonify(customers), 200

# Get order history by customer_id
@api_routes.route('/orders', methods=['GET'])
def fetch_all_orders():
    customer_id = request.args.get('customer_id')
    if customer_id:
        orders = get_order_history(int(customer_id))
        return jsonify(orders), 200
    return jsonify({'message': 'Customer ID not provided'}), 400

# Add a new menu item
@api_routes.route('/menu', methods=['POST'])
def create_menu_item():
    data = request.json
    add_menu_item(data['name'], data['price'])
    return jsonify({'message': 'Menu item added successfully!'}), 201

# Add a new customer
@api_routes.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    add_customer(data['name'], data['phone_number'])
    return jsonify({'message': 'Customer added successfully!'}), 201

# Place a new order
@api_routes.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    place_order(data['customer_id'], data['item_id'], data['quantity'])
    return jsonify({'message': 'Order placed successfully!'}), 201
