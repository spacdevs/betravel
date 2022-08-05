from ward import test
from flask import url_for
from __tests__.factories.category import CategoryFactory

from __tests__.factories.post import PostFactory
from __tests__.factories.user import UserFactory
from __tests__.fixtures import browser, login_as


@test("visitors view post details")
def _(browser=browser):
    post = PostFactory(title="Sobrevivendo ao frio da alemanha em Janeiro")

    browser.visit(url_for("home.index"))
    browser.links.find_by_text("Sobrevivendo ao frio da alemanha em Janeiro").click()

    assert browser.status_code == 200
    assert browser.is_text_present(post.title)
    assert browser.is_text_present(post.text)


@test("user create post", tags=['post'])
def _(browser=browser):
    user = UserFactory.build(password="123456")
    category = CategoryFactory.create(name="Europa")

    login_as(user, browser)
    browser.visit(url_for("home.index"))
    browser.links.find_by_text("Nova postagem").click()
    browser.fill("title", "Sobrevivendo ao frio da alemanha em Janeiro")
    browser.fill("text", "Primeiro precisamos nos agasalhar bastante...")
    browser.select("categories", str(category.id))
    browser.check("publish")
    browser.find_by_value("Cadastrar").click()

    assert browser.status_code == 200
    assert browser.url == url_for('home.index')
    assert browser.is_text_present("Sobrevivendo ao frio da alemanha em Janeiro")
