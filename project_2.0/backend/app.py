from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from backend.controllers.menu_controller import handle_menu_request
from backend.utils.utils import send_json_response, read_request_data

PORT = 8080

class RequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow all origins
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')  # Allow specific methods
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(200)
        self.wfile.write(b'')  # Respond with an empty body

    def do_GET(self):
        if self.path.startswith('/menu'):
            query = self.path.split('?')[1] if '?' in self.path else ''
            params = parse_qs(query)
            try:
                if 'item_id' in params:
                    item_id = params['item_id'][0]
                    response = handle_menu_request({'method': 'GET'}, {'item_id': item_id})
                else:
                    response = handle_menu_request({'method': 'GET'}, {})
                
                # Correct header setting
                self._set_headers(200)
                send_json_response(self, response)
            except Exception as e:
                self._set_headers(500)
                send_json_response(self, {"status": "error", "message": str(e)}, error_code=500)
        else:
            self._set_headers(404)
            send_json_response(self, {"status": "error", "message": "Not Found"}, error_code=404)

    def do_POST(self):
        if self.path == '/menu':
            try:
                data = read_request_data(self)
                response = handle_menu_request({'method': 'POST'}, data)
                self._set_headers(201)
                send_json_response(self, response)
            except Exception as e:
                self._set_headers(500)
                send_json_response(self, {"status": "error", "message": str(e)}, error_code=500)

    def do_PUT(self):
        if self.path == '/menu':
            try:
                data = read_request_data(self)
                if 'item_id' not in data:
                    self._set_headers(400)
                    send_json_response(self, {"status": "error", "message": "Item ID is required for update."}, error_code=400)
                    return
                response = handle_menu_request({'method': 'PUT'}, data)
                self._set_headers(200)
                send_json_response(self, response)
            except Exception as e:
                self._set_headers(500)
                send_json_response(self, {"status": "error", "message": str(e)}, error_code=500)

    def do_DELETE(self):
        if self.path == '/menu':
            try:
                data = read_request_data(self)
                if 'item_id' not in data:
                    self._set_headers(400)
                    send_json_response(self, {"status": "error", "message": "Item ID is required for deletion."}, error_code=400)
                    return
                response = handle_menu_request({'method': 'DELETE'}, data)
                self._set_headers(200)
                send_json_response(self, response)
            except Exception as e:
                self._set_headers(500)
                send_json_response(self, {"status": "error", "message": str(e)}, error_code=500)

    # Handling a hypothetical recover method
    def do_RECOVER(self):
        if self.path == '/menu/recover':
            try:
                data = read_request_data(self)
                if 'item_id' not in data:
                    self._set_headers(400)
                    send_json_response(self, {"status": "error", "message": "Item ID is required for recovery."}, error_code=400)
                    return
                response = handle_menu_request({'method': 'RECOVER'}, data)
                self._set_headers(200)
                send_json_response(self, response)
            except Exception as e:
                self._set_headers(500)
                send_json_response(self, {"status": "error", "message": str(e)}, error_code=500)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=PORT):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server is running at http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
