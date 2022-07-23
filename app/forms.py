from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class SignUpForm(FlaskForm):
    name = StringField(
        "Nome", validators=[DataRequired(), Length(min=6, max=120)]
    )
    email = EmailField(
        "E-mail", validators=[DataRequired(), Length(min=6, max=84)]
    )
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Registrar")
