from ward import test
from flask import url_for
from werkzeug.security import generate_password_hash

from tests.factories.user import UserFactory
from tests.fixtures import browser, login_as as login_fixture


@test("user create category")
def _(login_as=login_fixture, browser=browser):
    user = UserFactory.create(password=generate_password_hash("123456"))

    login_as(user)
    browser.visit(url_for('home.index'))
    browser.links.find_by_text("Nova categoria").click()
    browser.fill("title", "Europa")
    browser.links.find_by_text("Cadastrar").click()

    assert browser.status_code == 200
    assert browser.is_text_present("Europa")
