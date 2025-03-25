MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'  
MYSQL_PASSWORD = '301909'
MYSQL_DB = 'flask_api'
JWT_SECRET_KEY = 'Yashvi12223'  # For JWT token generation
# UPLOAD_FOLDER = 'app/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2 MB

import os

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')  