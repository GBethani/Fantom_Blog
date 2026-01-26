from django.contrib import admin
from . import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ['published_at', 'categories']
    list_display = ['slug', 'published_at', 'get_categories']
    search_fields = ['title', 'body']
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("categories",)

    def get_categories(self, obj):
        # Join category names into a readable string
        return ", ".join(cat.title for cat in obj.categories.all())

    get_categories.short_description = "Categories"

admin.site.register(models.Post, PostAdmin)