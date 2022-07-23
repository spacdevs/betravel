from ward import test
from flask import url_for
from werkzeug.security import generate_password_hash

from tests.fixtures import browser
from tests.factories.user import UserFactory


@test("visitors can do sign in")
def _(browser=browser):
    user = UserFactory.create(password=generate_password_hash("hehearsme"))

    browser.visit("/")
    browser.find_by_text("Entrar").click()
    browser.fill("email", user.email)
    browser.fill("password", "hehearsme")
    browser.find_by_value("Acessar").click()

    assert browser.url == url_for("home.index")
    assert browser.is_text_present(f"Bem-vindo de volta, {user.name}")
    assert browser.is_text_present(f"Olá, {user.name}")
    assert browser.is_text_present("Nova postagem")
    assert browser.is_text_present("Nova categoria")
    assert browser.is_text_present("Sair")
