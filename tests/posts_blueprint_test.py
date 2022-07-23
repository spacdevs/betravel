from ward import test
from flask import url_for

from tests.factories.post import PostFactory
from tests.fixtures import browser


@test("visitors view post details")
def _(browser=browser):
    post = PostFactory(title="Sobrevivendo ao frio da alemanha em Janeiro")

    browser.visit(url_for("home.index"))
    browser.links.find_by_text(
        "Sobrevivendo ao frio da alemanha em Janeiro"
    ).click()

    assert browser.status_code == 200
    assert browser.is_text_present(post.title)
    assert browser.is_text_present(post.text)
