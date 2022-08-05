from faker import Faker
from flask_seeder import Seeder

from app.models import Category

faker = Faker()


class CategorySeeder(Seeder):
    def run(self):
        for _ in range(2):
            category = Category(name=faker.country())
            print("Adicionando categoria: %s" % category.name)
            self.db.session.add(category)
