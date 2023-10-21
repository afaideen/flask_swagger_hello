
from flasgger import Swagger
from flask import Flask
from flask_restful import Api, Resource

# Run swagger with http://127.0.0.1:5000/apidocs
app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'My Test API Hello',
    'uiversion': 3,
    'doc_dir': '/apidocs/',
    'config': {
        'app-name': 'test'  # Change 'test' to your desired category label
    }
}
api = Api(app)

swagger = Swagger(app)

@app.route('/')
def hello():
    """
    A simple endpoint that returns 'Hi there! How are you?'.
    ---
    responses:
        200:
            description: Hi there! How are you?
    """
    return "Hi there! How are you?"



if __name__ == '__main__':
    app.run(debug=True)

