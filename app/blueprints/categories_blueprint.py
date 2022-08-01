from flask import Blueprint, render_template

# from app.models import Post

categories = Blueprint("categories", __name__)


@categories.get("/categories")
def new():
    # post = Post.query.get(id)
    return render_template("categories/mew.jinja")
