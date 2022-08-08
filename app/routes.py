from mvc_flask import Router


Router.get("/", "home#index")
Router.all("posts", only="show new create")

from app.blueprints.categories_blueprint import categories
from app.blueprints.sessions.sign_up_blueprint import sign_up
from app.blueprints.sessions.sign_in_blueprint import sign_in


def init_app(app):
    app.register_blueprint(sign_in)
    app.register_blueprint(sign_up)
    app.register_blueprint(categories)
