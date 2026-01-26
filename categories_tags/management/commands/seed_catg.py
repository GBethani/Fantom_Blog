from django.utils.text import slugify
from django.core.management.base import BaseCommand
from faker import Faker
from categories_tags.models import Category

faker = Faker()

class Command(BaseCommand):

    help = "seed database with fake categories"

    def add_arguments(self, parser):
        parser.add_argument('--total',type=int,default=10,help="number of categories to create")

    def handle(self, *args, **options):
        total = options['total']
        count = 0
        while count < total:
            name = faker.unique.word().capitalize()
            name_slug = slugify(name)
            if Category.objects.filter(slug=name_slug).exists():
                continue
            Category.objects.create(
                title=name,
                slug=name_slug
            )
            count+=1
        self.stdout.write(
            self.style.SUCCESS(f"{count} categories created")
        )