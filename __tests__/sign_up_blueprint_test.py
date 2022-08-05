from ward import test
from flask import url_for

from __tests__.fixtures import browser


@test("visitors can do sign up")
def _(browser=browser):
    browser.visit("/")
    browser.find_by_text("Cadastrar").click()
    browser.fill("name", "Marcus Pereira")
    browser.fill("email", "marcus@email.com")
    browser.fill("password", "hehearsme")
    browser.find_by_value("Registrar").click()

    assert browser.url == url_for("home.index")
    assert browser.is_text_present("Registro efetuado com sucesso!")
    assert browser.is_text_not_present("Olá, Marcus Pereira")
    assert browser.is_text_not_present("Nova Postagem")
    assert browser.is_text_not_present("Nova Categoria")
    assert browser.is_text_not_present("Sair")
