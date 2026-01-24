import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from posts.models import Post

fake = Faker()


class Command(BaseCommand):
    help = "Seed database with fake blog posts"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            type=int,
            default=10,
            help="Number of posts to create",
        )

    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        User = get_user_model()
        users = User.objects.all()

        if not users.exists():
            self.stdout.write(self.style.ERROR("No users found"))
            return

        for _ in range(total):
            title = fake.sentence(nb_words=6)
            Post.objects.create(
                title=title,
                body="\n\n".join(fake.paragraphs(nb=5)),
                author=random.choice(users),
            )

        self.stdout.write(
            self.style.SUCCESS(f"{total} fake posts created")
        )
