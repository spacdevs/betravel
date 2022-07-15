from pytest import fixture
from splinter import Browser

from app import create_app

@fixture
def browser():
    app = create_app()
    browser = Browser('flask', app=app)
    return browser
