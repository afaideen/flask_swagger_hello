from flasgger import swag_from
from flask import Blueprint

hello = Blueprint("hello", __name__, url_prefix="/api/v1/hello1")
# Run swagger with http://127.0.0.1:5000/apidocs
@hello.get('/')
@swag_from('./hello.yaml')
def index():
    b = 1
    """
    A simple endpoint that returns 'Hi there! How are you?'.
    ---
    responses:
        200:
            description: Hi there! How are you?
    """
    return "Hi there! How are you?"