import factory
from faker import Faker


from app.extensions import db
from app.models import User

faker = Faker()


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    name = faker.name()
    email = faker.email()
