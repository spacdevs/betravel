from app.blueprints.home_blueprint import home
from app.blueprints.posts_blueprint import posts
from app.blueprints.sessions.sign_up_blueprint import sign_up


def init_app(app):
    app.register_blueprint(home)
    app.register_blueprint(posts)
    app.register_blueprint(sign_up)
