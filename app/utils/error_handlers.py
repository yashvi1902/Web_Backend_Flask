# app/utils/error_handlers.py

from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify(message="Bad Request"), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify(message="Unauthorized"), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(message="Not Found"), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify(message="Internal Server Error"), 500
