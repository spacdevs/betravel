from dotenv import load_dotenv
from ward import fixture
from splinter import Browser

from app import create_app
from app.extensions import db

load_dotenv(".test.env")


@fixture
def browser():
    app = create_app()
    app.testing = True
    app_context = app.test_request_context()
    app_context.push()

    with app.test_client():
        db.create_all()

        yield Browser("flask", app=app)

        db.session.remove()
        db.drop_all()


@fixture
def login_as(user,browser=browser):
    breakpoint()
    # browser.visit("/")
    # browser.find_by_text("Entrar").click()
    # browser.fill("email", user.email)
    # browser.fill("password", user.password)
    # browser.find_by_value("Acessar").click()