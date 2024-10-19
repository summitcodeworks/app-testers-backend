from flask import jsonify
import re
from functools import wraps
from flask import request
from app.models.user import User
import logging

def create_response(response_code, response_message, data=None):
    """Create a standardized response."""
    response_body = {
        "header": {
            "responseCode": response_code,
            "responseMessage": response_message
        },
        "response": data
    }
    return jsonify(response_body), response_code

def extract_package_name(link):
    """Extract the package name from Play Store or app store links."""
    # First, try to extract package name from Play Store URL
    match = re.search(r'id=([a-zA-Z0-9._]+)', link)
    if match:
        return match.group(1)  # Return only the package name

    # If not found, try another common pattern for Android package names (for non-Play Store links)
    match = re.search(r'([a-zA-Z0-9._]+)', link)
    if match:
        return match.group(1)

    return None


def user_key_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_key = request.headers.get('api-key')
        print(f"Headers received: {request.headers}")  # Log all headers

        if not user_key:
            print("No user key provided")
            return create_response(401, "Api key is required", None)

        user = User.query.filter_by(user_key=user_key).first()
        print(f"User found: {user}")  # Debugging

        if not user:
            print("Invalid API key")
            return create_response(401, "Invalid api key", None)

        return f(*args, **kwargs)

    return decorated_function


