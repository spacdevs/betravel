import os
from flask import redirect, render_template, url_for, flash, current_app
from werkzeug.utils import secure_filename
from flask_login import current_user, login_required

from app.models import Post
from app.forms import PostForm
from app.extensions import db


class PostsController:
    def show(self, id):
        post = Post.query.get(id)
        return render_template("posts/show.jinja", post=post)

    @login_required
    def new(self):
        form = PostForm()
        return render_template("posts/new.jinja", form=form)

    @login_required
    def create(self):
        form = PostForm()

        if form.validate_on_submit():
            f = form.image.data
            filename = secure_filename(f.filename)
            f.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
            post = Post(
                title=form.title.data,
                text=form.text.data,
                image_name=filename,
                publish=form.publish.data,
                category_id=form.categories.data,
                author=current_user,
            )

            db.session.add(post)
            db.session.commit()
            flash("Post cadastrado com sucesso")
            return redirect(url_for("home.index"), 302)
        return render_template("posts/new.jinja", form=form)
