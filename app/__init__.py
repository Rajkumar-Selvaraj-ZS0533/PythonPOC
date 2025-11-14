from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_object='app.config.Config'):
    app = Flask(__name__)
    
    DB_USER = 'postgres'
    DB_PASSWORD = 'Password%401'
    DB_NAME = 'myflaskapp'
    DB_HOST = 'localhost'
    DB_PORT = '5432'

    # Configure app
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register blueprints
    from .controllers.user_controller import user_bp
    app.register_blueprint(user_bp)

    return app