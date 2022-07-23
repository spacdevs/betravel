from app.blueprints.home_blueprint import home
from app.blueprints.posts_blueprint import posts


def init_app(app):
    app.register_blueprint(home)
    app.register_blueprint(posts)
