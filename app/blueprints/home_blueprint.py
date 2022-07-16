from flask import Blueprint, render_template

from app.models import Post

home = Blueprint('home', __name__)

@home.get('/')
def index():
    posts = Post.query.all()

    return render_template('home/index.jinja', posts=posts)
