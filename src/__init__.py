from flasgger import Swagger
from flask import Flask
from flask_restful import Api

from src.hello import hello


def create_app():
    app = Flask(__name__)
    app.config['SWAGGER'] = {
        'title': 'My Test API Hello',
        'uiversion': 3,
        'doc_dir': '/apidocs/',
        'config': {
            'app-name': 'test'  # Change 'test' to your desired category label
        }
    }
    # api = Api(app)
    app.register_blueprint(hello)
    Swagger(app)

    return app

