import factory
from faker import Faker

from app.extensions import db
from app.models import Category

faker = Faker()


class CategoryFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Category
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    name = faker.text()
