from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Инициализация SQLAlchemy
db = SQLAlchemy()

def create_app():
    """Инациализация приложения, базы данных и блупринта."""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo_db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
