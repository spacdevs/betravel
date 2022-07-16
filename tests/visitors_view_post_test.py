from app.models import Post
from app import db

def test_successfully(browser):
    browser.visit("/")

    assert browser.status_code == 200
    assert browser.is_text_present("Viagens")
    assert browser.is_text_present("&COPY; Todos os direitos reservados. Be Travel 2022")
