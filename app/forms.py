from flask_wtf import FlaskForm
from wtforms.fields import (
    BooleanField,
    EmailField,
    PasswordField,
    StringField,
    SubmitField,
    TextAreaField,
    SelectField,
)
from flask_wtf.file import FileField, FileAllowed, FileRequired, FileStorage
from wtforms.validators import DataRequired, Length

from app.models import Category


class PostForm(FlaskForm):
    title = StringField(
        "Título", validators=[DataRequired(message="é obrigatório")]
    )
    text = TextAreaField(
        "Texto", validators=[DataRequired(message="é obrigatório")]
    )
    publish = BooleanField("Publicar")
    submit = SubmitField("Cadastrar")
    categories = SelectField(
        "Categorias", coerce=int, validators=[DataRequired()]
    )

    def __init__(self):
        super(PostForm, self).__init__()
        self.categories.choices = [
            (category.id, category.name) for category in Category.query.all()
        ]


class CategoryForm(FlaskForm):
    name = StringField(
        "Nome", validators=[DataRequired(message="é obrigatório")]
    )
    submit = SubmitField("Cadastrar")


class SignInForm(FlaskForm):
    email = EmailField(
        "E-mail",
        validators=[
            DataRequired(message="é obrigatório"),
            Length(min=6, max=84),
        ],
    )
    password = PasswordField(
        "Senha", validators=[DataRequired(message="é obrigatório")]
    )
    submit = SubmitField("Acessar")


class SignUpForm(FlaskForm):
    name = StringField(
        "Nome",
        validators=[
            DataRequired(message="é obrigatório"),
            Length(min=6, max=120),
        ],
    )
    email = EmailField(
        "E-mail",
        validators=[
            DataRequired(message="é obrigatório"),
            Length(min=6, max=84),
        ],
    )
    password = PasswordField(
        "Senha", validators=[DataRequired(message="é obrigatório")]
    )
    submit = SubmitField("Registrar")
