
from flask import Flask
from flask_mysqldb import MySQL
from flask_jwt_extended import JWTManager
from .utils.error_handlers import register_error_handlers
from .config import UPLOAD_FOLDER

mysql = MySQL()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    # Initialize MySQL and JWT
    mysql.init_app(app)
    jwt.init_app(app)

    # Error handling
    register_error_handlers(app)

    # Import and register blueprints (modular routes)
    from .controllers.auth_controller import auth_bp
    from .controllers.public_controller import public_bp
    from .controllers.file_controller import file_bp
    from .controllers.db_controller import db_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(public_bp)
    app.register_blueprint(file_bp)
    app.register_blueprint(db_bp)

    return app
