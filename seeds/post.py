from faker import Faker
from flask_seeder import Seeder

from app.models import Category, Post, User

faker = Faker()


class PostSeeder(Seeder):
    def run(self):
        user = User(email=faker.email(), name=faker.name(), password="123456")
        for _ in range(5):
            category = Category.query.first()
            post = Post(
                title=faker.paragraph(),
                text=faker.text(),
                publish=True,
                category=category,
                author=user,
            )
            print("Adicionando post: %s" % post.title)
            self.db.session.add(post)
