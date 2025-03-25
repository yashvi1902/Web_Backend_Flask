
import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from ..config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS, MAX_FILE_SIZE

file_bp = Blueprint('file_bp', __name__)

# Function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Upload endpoint
@file_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        print("files", request.files)
        return jsonify(message="No file part"), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify(message="No selected file"), 400

    if not allowed_file(file.filename):
        return jsonify(message="File type not allowed"), 400

    if len(file.read()) > MAX_FILE_SIZE:
        return jsonify(message="File is too large"), 400

    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    print("Upload Folder:", UPLOAD_FOLDER)
    return jsonify(message="File uploaded successfully", filename=filename), 200
