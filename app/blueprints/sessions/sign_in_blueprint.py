from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_user
from werkzeug.security import check_password_hash

from app.forms import SignInForm
from app.models import User


sign_in = Blueprint("signin", __name__)


@sign_in.get("/conta/acessar")
def new():
    form = SignInForm()
    return render_template("sessions/sign_in/new.jinja", form=form)


@sign_in.post("/conta/acessar")
def create():
    form = SignInForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if not user or not check_password_hash(
            user.password, form.password.data
        ):
            flash("Usúario ou senha estão incorretas")
            return redirect(url_for(".new"))

        login_user(user)
        flash(f"Bem-vindo de volta, {user.name}")
        return redirect(url_for("home.index"))

    return render_template("sessions/sign_in/new.jinja", form=form)
