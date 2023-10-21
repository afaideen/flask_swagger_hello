
from src.app import  create_app

# Run swagger with http://127.0.0.1:5000/apidocs

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

