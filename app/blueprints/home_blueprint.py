from flask import Blueprint

home = Blueprint('home', __name__)

@home.get('/')
def index():
    return 'Olá, Flask!'
