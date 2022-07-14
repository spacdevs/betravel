from venv import create
from pytest import fixture
from splinter import Browser
from app import create_app


@fixture
def browser():
    app = create_app()
    browser = Browser('flask', app=app)
    return browser


def test_visitors_view_home_page_successfully(browser):
    browser.visit('/')

    assert browser.status_code == 200
    assert browser.is_text_present('Olá, Flask!')