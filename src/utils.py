from flask import jsonify, Response


def generate_message_response(message, response_code=200):
    return jsonify({
        "message": message
    }), response_code
