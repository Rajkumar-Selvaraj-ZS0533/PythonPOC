# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)


# DB_USER = 'postgres'
# DB_PASSWORD = 'Password%401'
# DB_NAME = 'myflaskdb'
# DB_HOST = 'localhost'
# DB_PORT = '5432'


# app.config['SQLALCHEMY_DATABASE_URI'] = (
#         f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
#     )
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# from models.user import user

# if __name__ == '__main__' :
#     app.run(debug=True)


# run.py
from flask import Flask
from app import create_app


# Initialize db, but don't tie it to any app yet
# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)
#     DB_USER = 'postgres'
#     DB_PASSWORD = 'Password%401'
#     DB_NAME = 'myflaskapp'
#     DB_HOST = 'localhost'
#     DB_PORT = '5432'

#     # Configure app
#     app.config['SQLALCHEMY_DATABASE_URI'] = (
#         f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
#     )
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     # Initialize db with the app
#     db.init_app(app)

#     # # Import models here after db initialization to avoid circular import
#     # from app.models.user import User

#     from app.controllers.user_controller import user_bp
#     app.register_blueprint(user_bp)
#     print ("completed the db")

#     return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
