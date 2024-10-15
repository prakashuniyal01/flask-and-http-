from models.order import get_order_history, place_order

def handle_order_request(request):
    if request['method'] == 'POST':
        data = request['body']
        customer_id = data['customer_id']
        item_id = data['item_id']
        quantity = data['quantity']
        order_date = data['order_date']
        place_order(customer_id, item_id, quantity, order_date)
        return {"status": "success", "message": "Order placed"}
    
    elif request['method'] == 'GET':
        customer_id = request['query'].get('customer_id')
        if customer_id:
            history = get_order_history(customer_id)
        else:
            history = get_order_history()
        
        # Return empty list if no data found
        if not history:
            history = []
        
        return {"status": "success", "data": history}
