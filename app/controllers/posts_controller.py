from flask import redirect, render_template, url_for, flash
from flask_login import current_user

from app.models import Post
from app.forms import PostForm
from app.extensions import db


class PostsController:
    def show(self, id):
        post = Post.query.get(id)
        return render_template("posts/show.jinja", post=post)

    def new(self):
        form = PostForm()
        return render_template("posts/new.jinja", form=form)

    def create(self):
        form = PostForm()

        if form.validate_on_submit():
            post = Post(
                title=form.title.data,
                text=form.text.data,
                publish=form.publish.data,
                category_id=form.categories.data,
                author=current_user,
            )
            db.session.add(post)
            db.session.commit()

            flash("Post cadastrado com sucesso")
            return redirect(url_for("home.index"))

        return render_template("posts/new.jinja", form=form)
