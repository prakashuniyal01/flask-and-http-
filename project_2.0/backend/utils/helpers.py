from datetime import datetime

def format_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').strftime('%d-%b-%Y')

def calculate_total_revenue(orders):
    return sum(order['price'] * order['quantity'] for order in orders)
