from django import template
from django.db.models import Count
from categories_tags.models import Category
from categories_tags.querysets import categories_with_post_count

register = template.Library()

@register.inclusion_tag('categories_tags/tag_cloud.html')
def category_tag_cloud():
    return {'categories': categories_with_post_count}