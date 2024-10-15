from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import decimal
from urllib.parse import urlparse, parse_qs
from controllers.menu_controller import handle_menu_request
from controllers.order_controller import handle_order_request
from controllers.customer_controller import handle_customer_request
from datetime import date

# Custom JSON Encoder to handle Decimal types
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        if isinstance(obj, date):  # Convert date objects to strings
            return obj.isoformat()  # Convert to 'YYYY-MM-DD'
        return super(DecimalEncoder, self).default(obj)


class RequestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def parse_query(self):
        """Parse query parameters from the URL."""
        parsed_url = urlparse(self.path)
        return {k: v[0] for k, v in parse_qs(parsed_url.query).items()}  # Get single value

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        request = {'method': 'GET'}
        
        if self.path.startswith('/menu'):
            response = handle_menu_request(request)
            self.wfile.write(json.dumps(response, cls=DecimalEncoder).encode())
        
        elif self.path.startswith('/customers'):
            response = handle_customer_request(request)
            self.wfile.write(json.dumps(response, cls=DecimalEncoder).encode())
        
        elif self.path.startswith('/order'):
            query_params = self.parse_query()
            customer_id = query_params.get('customer_id', None)
            response = handle_order_request({"method": "GET", "query": {"customer_id": customer_id}})
            self.wfile.write(json.dumps(response, cls=DecimalEncoder).encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        request = {'method': 'POST'}
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode())
        
        if self.path.startswith('/menu'):
            response = handle_menu_request(request, data)
            self.wfile.write(json.dumps(response, cls=DecimalEncoder).encode())
        
        elif self.path.startswith('/customers'):
            response = handle_customer_request(request, data)
            self.wfile.write(json.dumps(response, cls=DecimalEncoder).encode())
            
        elif self.path.startswith('/order'):
            response = handle_order_request({"method": "POST", "body": data})
            if response.get("success"):
                self.send_response(201)
            else:
                self.send_response(400)
            self.wfile.write(json.dumps(response, cls=DecimalEncoder).encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
