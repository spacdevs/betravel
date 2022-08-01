from ward import test
from flask import url_for
from app.models import Category

from tests.factories.user import UserFactory
from tests.fixtures import browser, login_as as login_fixture


@test("user create category")
def _(login_as=login_fixture, browser=browser):
    user = UserFactory.build(password="123456")

    login_as(user, browser)
    browser.visit(url_for("home.index"))
    browser.links.find_by_text("Nova categoria").click()
    browser.fill("name", "Europa")
    browser.find_by_value("Cadastrar").click()

    assert browser.status_code == 200
    assert browser.url == url_for("categories.new")
    assert Category.query.first().name == "Europa"
