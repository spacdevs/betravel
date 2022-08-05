from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder

db = SQLAlchemy()
login_manager = LoginManager()


def init_app(app):
    login_manager.init_app(app)
    db.init_app(app)
    FlaskSeeder(app, db)
    Migrate(app, db)

    @app.shell_context_processor
    def _():
        from app.models import Category, User, Post

        return dict(Category=Category, Post=Post, User=User)
