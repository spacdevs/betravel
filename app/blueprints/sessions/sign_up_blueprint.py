from flask import Blueprint, flash, redirect, render_template, url_for
from werkzeug.security import generate_password_hash

from app.forms import SignUpForm
from app.extensions import db
from app.models import User


sign_up = Blueprint("signup", __name__)


@sign_up.get("/conta/registro")
def new():
    form = SignUpForm()
    return render_template("sessions/sign_up/new.jinja", form=form)


@sign_up.post("/conta/registro")
def create():
    form = SignUpForm()

    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data),
        )
        db.session.add(user)
        db.session.commit()

        flash("Registro efetuado com sucesso!")
        return redirect(url_for("home.index"))
    
    return render_template("sessions/sign_up/new.jinja", form=form)
