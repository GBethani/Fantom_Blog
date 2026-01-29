from django.db.models import Count
from .models import Category

def categories_with_post_count():
    return Category.objects.annotate(
        post_count=Count('post')
    ).filter(post_count__gt=0)
