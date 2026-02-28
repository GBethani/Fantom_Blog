import os
import random
from django.core.management.base import BaseCommand
from posts.models import Post

class Command(BaseCommand):
    help = "Replace all post images with random placeholders"

    def handle(self, *args, **kwargs):
        placeholder_dir = "media/placeholders"
        images = os.listdir(placeholder_dir)

        for post in Post.objects.all():
            random_image = random.choice(images)
            post.image = f"placeholders/{random_image}"
            post.save()

        self.stdout.write(self.style.SUCCESS("Images replaced successfully"))