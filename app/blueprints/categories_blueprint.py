from flask import flash
from flask import Blueprint, redirect, render_template, url_for

from app.forms import CategoryForm
from app.models import Category
from app.extensions import db

categories = Blueprint("categories", __name__)


@categories.get("/categories")
def new():
    form = CategoryForm()
    return render_template("categories/new.jinja", form=form)


@categories.post("/categories")
def create():
    form = CategoryForm()

    if form.validate_on_submit():
        category = Category(name=form.name.data)
        db.session.add(category)
        db.session.commit()

        flash("categoria cadastrada com sucesso")
        return redirect(url_for(".new"))

    return render_template("categories/new.jinja", form=form)
