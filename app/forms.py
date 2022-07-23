from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class SignInForm(FlaskForm):
    email = EmailField(
        "E-mail", validators=[DataRequired(message='é obrigatório'), Length(min=6, max=84)]
    )
    password = PasswordField("Senha", validators=[DataRequired(message='é obrigatório')])
    submit = SubmitField("Acessar")


class SignUpForm(FlaskForm):
    name = StringField(
        "Nome", validators=[DataRequired(message='é obrigatório'), Length(min=6, max=120)]
    )
    email = EmailField(
        "E-mail", validators=[DataRequired(message='é obrigatório'), Length(min=6, max=84)]
    )
    password = PasswordField("Senha", validators=[DataRequired(message='é obrigatório')])
    submit = SubmitField("Registrar")
