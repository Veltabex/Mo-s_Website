

# Flask web server to serve static files
from flask import Flask, send_from_directory
import os

# Path to your mirrored site - files are in the same folder as this script
STATIC_FOLDER = "."
TEMPLATES_FOLDER = "templates"


app = Flask(__name__, static_folder=STATIC_FOLDER, static_url_path='')

@app.route('/')
def index():
    return send_from_directory(TEMPLATES_FOLDER, 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    # Check if it's an HTML file first - serve from templates folder
    if path.endswith('.html'):
        safe_path = os.path.join(TEMPLATES_FOLDER, path)
        if not os.path.abspath(safe_path).startswith(os.path.abspath(TEMPLATES_FOLDER)):
            return "Access Denied", 403
        return send_from_directory(TEMPLATES_FOLDER, path)
    
    # For non-HTML files, serve from static folder
    safe_path = os.path.join(STATIC_FOLDER, path)
    if not os.path.abspath(safe_path).startswith(os.path.abspath(STATIC_FOLDER)):
        return "Access Denied", 403
    return send_from_directory(STATIC_FOLDER, path)


if __name__ == '__main__':
    # Start Flask app
    app.run(port=5000, debug=True)