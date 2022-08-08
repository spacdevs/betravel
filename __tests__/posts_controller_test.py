import io
from ward import test
from flask import url_for
from __tests__.factories.category import CategoryFactory

from __tests__.factories.post import PostFactory
from __tests__.factories.user import UserFactory
from __tests__.fixtures import browser, login_as, client


@test("visitors view post details")
def _(browser=browser):
    post = PostFactory.create(
        title="Sobrevivendo ao frio da alemanha em Janeiro"
    )
    browser.visit(url_for("home.index"))
    browser.links.find_by_partial_text(
        "Sobrevivendo ao frio da alemanha em Janeiro"
    ).click()

    assert browser.status_code == 200
    assert browser.is_text_present(post.title)
    assert browser.is_text_present(post.text)


@test("user create post", tags=["post"])
def _(client=client):
    user = UserFactory.create(password="123456")
    category = CategoryFactory.create(name="Europa")
    data = {
        "title": "Sobrevivendo ao frio da alemanha em Janeiro",
        "text": "Primeiro precisamos nos agasalhar bastante...",
        "categories": str(category.id),
        "image": (io.BytesIO(b"abcdef"), "grecia.jpg"),
        "publish": True,
    }

    client.post(
        url_for("signin.create"),
        data={"email": user.email, "password": "123456"},
        follow_redirects=True,
    )
    response = client.post(
        url_for("posts.create"), data=data, follow_redirects=True
    )

    assert response.status_code == 200
    assert "grecia.jpg" in response.get_data(as_text=True)
    assert "Sobrevivendo ao frio da alemanha em Janeiro" in response.get_data(
        as_text=True
    )
