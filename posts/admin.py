from django.contrib import admin
from . import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ['published_at']
    list_display = ['slug','published_at']
    search_fields = ['title','body']
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = models.Post

admin.site.register(models.Post,PostAdmin)
