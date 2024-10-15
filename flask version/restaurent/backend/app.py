from flask import Flask
from flask_cors import CORS
from routes import api_routes  # Import routes from routes.py

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Register the API routes from routes.py
app.register_blueprint(api_routes)

if __name__ == '__main__':
    app.run(debug=True)
