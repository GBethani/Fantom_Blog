from django.core.management.base import BaseCommand
from posts.models import Post
from ._image_helpers import attach_fake_image


class Command(BaseCommand):
    help = "Attach fake images to posts without images"

    def handle(self, *args, **kwargs):
        # Select posts where image field is either NULL or empty string
        posts = (
            Post.objects.filter(image__isnull=True)
            | Post.objects.filter(image="")
        )

        # If no such posts exist, stop early
        if not posts.exists():
            self.stdout.write(
                self.style.WARNING("All posts already have images")
            )
            return

        # Attach fake images
        for post in posts:
            attach_fake_image(post)

        # Print success message
        self.stdout.write(
            self.style.SUCCESS(f"Images added to {posts.count()} posts")
        )
