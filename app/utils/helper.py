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
    # First, try to extract package name from Play Store URL
    match = re.search(r'id=([a-zA-Z0-9._]+)', link)
    if match:
        return match.group(1)  # Return only the package name

    # If not found, try another common pattern for Android package names (for non-Play Store links)
    match = re.search(r'([a-zA-Z0-9._]+)', link)
    if match:
        return match.group(1)

    return None
