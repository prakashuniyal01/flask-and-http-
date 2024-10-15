import json

def send_json_response(handler, response, success_code=200, error_code=400):
    # Set status code based on the response status
    status_code = success_code if response.get('status') == 'success' else error_code
    handler._set_headers(status_code)  # Ensure headers are set before sending the response
    
    # Convert response object to JSON and write to the output stream
    response_body = json.dumps(response).encode('utf-8')
    
    # Write only the JSON body
    handler.wfile.write(response_body)

def read_request_data(handler):
    try:
        content_length = int(handler.headers.get('Content-Length', 0))
        if content_length > 0:
            post_data = handler.rfile.read(content_length)
            return json.loads(post_data.decode('utf-8'))
        return {}
    except Exception as e:
        raise ValueError(f"Error reading request data: {str(e)}")
