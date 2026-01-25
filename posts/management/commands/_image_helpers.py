import random
from pathlib import Path
from django.core.files import File

PLACEHOLDER_DIR = Path("media/placeholders")


def attach_fake_image(post):
    """
    Attach a random placeholder image to a Post instance.
    Used ONLY for dev/testing data seeding.
    """

    images = list(PLACEHOLDER_DIR.glob("*.jpg"))
    if not images:
        return

    image_path = random.choice(images)

    with open(image_path, "rb") as f:
        post.image.save(
            image_path.name,
            File(f),
            save=True
        )
