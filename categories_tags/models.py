from django.db import models
from django.utils.text import slugify
import uuid
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, unique= True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            self.slug = f"{base}-{uuid.uuid4().hex[:6]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title