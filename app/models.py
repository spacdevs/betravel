from flask_login import UserMixin

from app.extensions import db, login_manager

@login_manager.user_loader
def get_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return self.name

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    published = db.Column(db.Boolean, default=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return self.title
