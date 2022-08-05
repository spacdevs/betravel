import factory
from faker import Faker

from app.extensions import db
from app.models import Post
from __tests__.factories.category import CategoryFactory
from __tests__.factories.user import UserFactory

faker = Faker()


class PostFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Post
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    title = faker.text()
    text = faker.paragraph()
    published = True
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
