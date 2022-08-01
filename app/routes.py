from app.blueprints.home_blueprint import home
from app.blueprints.posts_blueprint import posts
from app.blueprints.categories_blueprint import categories
from app.blueprints.sessions.sign_up_blueprint import sign_up
from app.blueprints.sessions.sign_in_blueprint import sign_in


def init_app(app):
    app.register_blueprint(home)
    app.register_blueprint(posts)
    app.register_blueprint(sign_in)
    app.register_blueprint(sign_up)
    app.register_blueprint(categories)
