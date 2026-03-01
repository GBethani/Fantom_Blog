from django.db import migrations
from django.utils import timezone
import random


def randomize_post_status(apps, schema_editor):
    """
    Forward migration:

    Iterate through ALL posts exactly once.
    Randomly assign each post as draft or published
    with approximately 50-50 distribution.
    """

    # Get historical Post model
    Post = apps.get_model("posts", "Post")

    # Convert QuerySet to list to avoid re-querying DB multiple times
    posts = list(Post.objects.all())

    for post in posts:

        # Generate random True/False
        is_published = random.choice([True, False])

        if is_published:
            # Set post as published
            post.status = "published"

            # Assign current timestamp
            post.published_at = timezone.now()
        else:
            # Set post as draft
            post.status = "draft"

            # Drafts should not have publish date
            post.published_at = None

        # Save changes to DB
        post.save()


def reverse_randomize_post_status(apps, schema_editor):
    """
    Reverse migration:

    Reset ALL posts back to draft.
    This is deterministic and safe.
    """

    Post = apps.get_model("posts", "Post")

    posts = Post.objects.all()

    for post in posts:
        post.status = "draft"
        post.published_at = None
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_status_alter_post_published_at'),
    ]

    operations = [
        migrations.RunPython(
            randomize_post_status,
            reverse_randomize_post_status
        ),
    ]