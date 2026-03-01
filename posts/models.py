from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone
from .upload_paths import upload_post_image
from categories_tags.models import Category
import uuid

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class Post(models.Model):
    STATUS_CHOICES = (
        ("draft","Draft"),
        ("published","Published")
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default="draft")

    objects = models.Manager()
    published = PublishedManager()

    published_at = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(blank=True,null=True,upload_to=upload_post_image)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            self.slug = f"{base}-{uuid.uuid4().hex[:6]}"
        if self.status == "published" and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    @classmethod
    def visible_to(cls, user):
        """
        Returns queryset of posts visible to given user.
        """

        if user.is_staff:
            return cls.objects.all()

        return cls.published.all()

    def __str__(self):
        return self.title
