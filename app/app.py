from flask import Flask
from app import create_app

# Create Flask app instance
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
