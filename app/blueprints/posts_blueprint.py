from flask import Blueprint, render_template

from app.models import Post

posts = Blueprint('posts', __name__)

@posts.get('/posts/<id>')
def show(id):
    post = Post.query.get(id)

    return render_template('posts/show.jinja', post=post)
