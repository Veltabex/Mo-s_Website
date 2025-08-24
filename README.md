# Website Flask Server

A simple Flask web server to serve static website files.

## Description

This Flask application serves static HTML, CSS, and JavaScript files from the current directory. It's designed to host a website locally or deploy to cloud platforms that support Python applications.

## Features

- Serves static files from the current directory
- Security protection against directory traversal attacks
- Simple and lightweight Flask application
- Easy to deploy to various hosting platforms

## Installation

1. Clone this repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running Locally

```bash
python website_scrapper.py
```

The server will start on `http://localhost:5000`

### File Structure

Make sure your website files (HTML, CSS, JS) are in the same directory as `website_scrapper.py`:

```
your-project/
├── website_scrapper.py
├── requirements.txt
├── index.html
├── style.css
├── script.js
└── other-assets/
```

## Deployment

This Flask app can be deployed to various hosting platforms:

- **Heroku**: Add a `Procfile` with `web: python website_scrapper.py`
- **Railway**: Works out of the box
- **Render**: Works out of the box
- **PythonAnywhere**: Upload files and configure WSGI

## Requirements

- Python 3.7+
- Flask 2.3.3

## License

This project is open source and available under the [MIT License](LICENSE).
