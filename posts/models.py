from django.db import models
from django.conf import settings
from django.utils.text import slugify
from .upload_paths import upload_post_image
import uuid

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True,null=True,upload_to=upload_post_image)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            self.slug = f"{base}-{uuid.uuid4().hex[:6]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
