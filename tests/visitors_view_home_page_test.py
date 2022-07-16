from flask import url_for
from faker import Faker

from app.models import Post
from app import db

def test_visitors_view_home_page_successfully(browser):
    browser.visit(url_for('home.index'))

    assert browser.status_code == 200
    assert browser.is_text_present("Viagens")
    assert browser.is_text_present("&COPY; Todos os direitos reservados. Be Travel 2022")

def test_visitors_view_menu(browser):
    browser.visit(url_for('home.index'))

    assert browser.is_text_present("Be Travel")
    assert browser.is_text_present("Nova Postagem")
    assert browser.is_text_present("Nova Categoria")
    assert browser.is_text_present("Entrar")
    assert browser.is_text_present("Olá, Marcus Pereira")
    assert browser.is_text_present("Sair")

def test_and_view_posts(browser):
    fake = Faker()
    post = Post(title=fake.paragraph(),
                published=True, text='Estava muito frio...')
    db.session.add(post)
    db.session.commit()

    browser.visit(url_for('home.index'))

    assert browser.is_text_present(post.title)

def test_and_not_view_posts(browser):   
    browser.visit(url_for('home.index'))

    assert browser.is_text_present("Sem posts cadastrado no momento")
