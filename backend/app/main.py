from flask import Flask
from flask_cors import CORS
from .config import Config
from .routes import register_routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Enable CORS
    CORS(app)
    
    # Register routes
    register_routes(app)
    
    return app

import os

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 8900))
    app.run(host='0.0.0.0', port=port, debug=False)