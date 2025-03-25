import os
from werkzeug.utils import secure_filename
from flask import current_app

def save_file(file):
    filename = secure_filename(file.filename)
    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
    return filename
