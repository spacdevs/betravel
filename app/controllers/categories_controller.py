from flask import flash
from flask import redirect, render_template, url_for
from flask_login import login_required

from app.forms import CategoryForm
from app.models import Category
from app.extensions import db


class CategoriesController:
    @login_required
    def new(self):
        form = CategoryForm()
        return render_template("categories/new.jinja", form=form)

    @login_required
    def create(self):
        form = CategoryForm()

        if form.validate_on_submit():
            category = Category(name=form.name.data)
            db.session.add(category)
            db.session.commit()

            flash("categoria cadastrada com sucesso")
            return redirect(url_for(".new"))

        return render_template("categories/new.jinja", form=form)
