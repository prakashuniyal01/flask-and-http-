from models.customer import add_customer, get_customers

def handle_customer_request(request, data=None):
    if request['method'] == 'POST':
        if data is None:  # Check if data is None
            return {
                "status": "error",
                "message": "No data provided"
            }
        
        # Ensure data has the required keys
        name = data.get('name')
        phone_number = data.get('phone_number')

        if name is None or phone_number is None:
            return {
                "status": "error",
                "message": "Missing name or phone number"
            }

        add_customer(name, phone_number)
        return {
            "status": "success",
            "message": "Customer added successfully"
        }
    
    elif request['method'] == 'GET':
        customer_list = get_customers()
        print(customer_list)
        return {
            "status": "success",
            "data": customer_list
        }
    
    return {
        "status": "error",
        "message": "Invalid request method"
    }
