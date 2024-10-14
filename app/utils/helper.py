from flask import jsonify
import re

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
    match = re.search(r'id=([a-zA-Z0-9._]+)', link) or re.search(r'com\.[a-zA-Z0-9._]+', link)
    if match:
        return match.group(0).replace('id=', '')
    return None
