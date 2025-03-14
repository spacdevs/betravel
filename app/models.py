from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from sqlalchemy import event

from app.extensions import db, login_manager


@login_manager.user_loader
def get_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    posts = db.relationship("Post", backref="author", uselist=True)

    def __repr__(self) -> str:
        return self.name


@event.listens_for(User, "before_insert")
def user_before_commit(mapper, connection, target):
    target.password = generate_password_hash(target.password)


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    publish = db.Column(db.Boolean, default=False)
    image_name = db.Column(db.String)
    text = db.Column(db.Text, nullable=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey("categories.id"), nullable=False
    )
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self) -> str:
        return self.title


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    posts = db.relationship("Post", backref="category", uselist=True)

    def __repr__(self) -> str:
        return self.name
