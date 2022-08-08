from mvc_flask import Router


Router.get("/",             "home#index")
Router.all("posts",         only="show new create")
Router.all("categories",    only="new create")
Router.all("signup",       only="new create")

from app.blueprints.sessions.sign_in_blueprint import sign_in

def init_app(app):
    app.register_blueprint(sign_in)
