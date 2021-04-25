from flask import Flask
from routes.request_handler import configure_routes

app = Flask(__name__)

configure_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
