from ward import test
from flask import url_for

from tests.factories.post import PostFactory
from tests.fixtures import browser


@test("Visitors access home page with successfully")
def _(browser=browser):
    browser.visit(url_for("home.index"))

    assert browser.status_code == 200
    assert browser.is_text_present("Viagens")
    assert browser.is_text_present(
        "&COPY; Todos os direitos reservados. Be Travel 2022"
    )


@test("Visitors access home page and view menu")
def _(browser=browser):
    browser.visit(url_for("home.index"))

    assert browser.is_text_present("Be Travel")
    assert browser.is_text_present("Nova Postagem")
    assert browser.is_text_present("Nova Categoria")
    assert browser.is_text_present("Entrar")
    assert browser.is_text_present("Olá, Marcus Pereira")
    assert browser.is_text_present("Sair")


@test("Visitors access home page and view posts")
def _(browser=browser):
    post = PostFactory()

    browser.visit(url_for("home.index"))

    assert browser.is_text_present(post.title)


@test("Visitors access home page and not view unplublished posts")
def _(browser=browser):
    post = PostFactory(title="Visitando a Apple em New York", published=False)

    browser.visit(url_for("home.index"))

    assert browser.is_text_not_present("Visitando a Apple em New York")
    assert browser.is_text_present("Sem posts cadastrado no momento")


@test("Visitors access home page and not view posts without registered")
def _(browser=browser):
    browser.visit(url_for("home.index"))

    assert browser.is_text_present("Sem posts cadastrado no momento")
