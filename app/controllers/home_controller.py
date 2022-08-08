from flask import render_template

from app.models import Post


class HomeController:
    def index(self):
        posts = Post.query.filter_by(publish=True).all()
        return render_template("home/index.jinja", posts=posts)
